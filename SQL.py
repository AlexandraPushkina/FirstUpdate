import mysql.connector
from mysql.connector import Error
from enum import Enum
from SQL_password import *


# theme = Enum('theme',['Nature','Technology','Social'])

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
    return str(cursor.fetchall())[3:-4]  # return str without unnecessary symbols ('[]')
    connection.close()



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
    query = 'SELECT history_text,history_done,date FROM words.users  INNER JOIN words.history ON users.id = history.iduser WHERE users.id = %s;'
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
    return str(cursor.fetchall())[3:-4]

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
        query = 'SELECT choice1,choice2,choice3 FROM words.irregular_words WHERE choice1 =%s OR choice2= %s OR choice3 = %s OR additional_choice = %s LIMIT 1;'
        cursor.execute(query, (word,word,word,word))
        for row in cursor.fetchall():
            ls.append(row)
        # connection.close()
        return (' '.join(*ls))  # get list  word word word
    except TypeError:
        try:
            ls = []
            cursor = connection.cursor(buffered=True)
            query2 = 'SELECT choice1,choice2,choice3,choice4 FROM words.regular_verbs WHERE choice1 = %s OR choice2= %s OR choice3 = %s OR choice4 = %s LIMIT 1;'
            cursor.execute(query2, (word, word, word,word))
            for row in cursor.fetchall():  #Переделать. Возвращает 0-ой индекс cursor.fetchall()[0]
                ls.append(row)  # get list with tuples [(text,date),....,(text,date)]
            # connection.close()
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
    print(name, password)
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
        print('False')
        connection.close()
        return False
    else:
        connection.close()
        print(result)
        return result[0]    #return id_user which linked with history

# print(get_text_by_theme(['Nature']))
# print(return_text_from_history([1]))
#register_new_user('Anna','2001.03')
#print(confirm_user('Sam','london'))
#print(confirm_user('Sam','london'))  #return Sam's texts
#print(return_user_name(confirm_user('Sam','london')))
print(len(cast_verbs('write').split()))