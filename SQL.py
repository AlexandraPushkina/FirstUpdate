import mysql.connector
from SQL_password import MySQL_password

def get_text_by_theme(theme):  # connection and query for database
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password=MySQL_password,
        database='words'
    )
    cursor = connection.cursor()
    query = 'SELECT text FROM words.text_collections WHERE theme = %s ORDER BY RAND() LIMIT 1;'  # query with parametr
    cursor.execute(query, (theme))
    text = str(cursor.fetchall())[3:-4]  # return str without unnecessary symbols ('[]')
    connection.close()
    return text


def save_in_history(text, date):
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password=MySQL_password,
        database='words'
    )
    cursor = connection.cursor()
    query = 'INSERT INTO words.history(history_text,date) VALUES ((%s),(%s))'
    cursor.execute(query, (text, date))
    connection.commit()
    connection.close()


def return_text_from_history(iduser):
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password=MySQL_password,
        database='words'
    )
    cursor = connection.cursor()
    query = 'SELECT history_text,date FROM words.users  INNER JOIN words.history ON users.id = history.iduser WHERE users.id = %s;'
    cursor.execute(query,(iduser))
    ls = []
    for row in cursor.fetchall():
        ls.append(row)  # get list with tuples [(text,date),....,(text,date)]
    connection.close()
    return ls

def return_user_name(user_id):
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password=MySQL_password,
        database='words'
    )
    cursor = connection.cursor()
    query = 'SELECT user_name FROM words.users WHERE id = %s'
    cursor.execute(query,(user_id))
    user_name = str(cursor.fetchall())[3:-4]
    connection.close()
    return user_name

def cast_verbs(word):  # return 3 or 4 words
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password=MySQL_password,
        database='words'
    )
    try:
        ls = []
        cursor = connection.cursor(buffered=True)
        query = 'SELECT choice1,choice2,choice3 FROM words.irregular_words WHERE choice1 =%s OR choice2= %s OR choice3 = %s LIMIT 1;'
        cursor.execute(query, (word,word,word))
        for row in cursor.fetchall():
            ls.append(row)
        return (' '.join(*ls))  # get list  word word word
    except TypeError:
        try:
            ls = []
            cursor = connection.cursor(buffered=True)
            query2 = 'SELECT choice1,choice2,choice3,choice4 FROM words.regular_verbs WHERE choice1 = %s OR choice2= %s OR choice3 = %s OR choice4 = %s LIMIT 1;'
            cursor.execute(query2, (word, word, word,word))
            for row in cursor.fetchall():  #Переделать. Возвращает 0-ой индекс cursor.fetchall()[0]
                ls.append(row)  # get list with tuples [(text,date),....,(text,date)]
            return (' '.join(*ls))
        except TypeError:
            connection.close()
            return False
def register_new_user(name, password):
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password=MySQL_password,
        database='words'
    )
    query = 'INSERT INTO words.users (user_name, user_password) VALUES ((%s),(%s))'
    cursor = connection.cursor()
    cursor.execute(query, (name,password))
    connection.commit()
    connection.close()

def confirm_user(name, password):
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password=MySQL_password,
        database='words'
    )
    cursor = connection.cursor()
    query = 'SELECT users.id FROM words.users WHERE user_name = %s AND user_password = %s'
    cursor.execute(query,(name,password))
    ls = []
    result = cursor.fetchall()
    if result is None:
        connection.close()
        return False
    else:
        connection.close()
        return result[0]    #return id_user which linked with history
