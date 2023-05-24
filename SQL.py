import mysql.connector
from mysql.connector import Error
from enum import Enum


# theme = Enum('theme',['Nature','Technology','Social'])

def get_text_by_theme(theme):  # connection and query for database
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='Mshrmwllpsnu1',
        database='words'
    )
    cursor = connection.cursor()
    query = 'SELECT text FROM words.text_collections WHERE theme = %s ORDER BY RAND() LIMIT 1;'  # query with parametr
    cursor.execute(query, (theme,))
    connection.close()
    return str(cursor.fetchall())[3:-4]  # return str without unnecessary symbols ('[]')


def save_in_history(text, date):
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='Mshrmwllpsnu1',
        database='words'
    )
    cursor = connection.cursor()
    query = 'INSERT INTO words.history(history_text,date) VALUES ((%s),(%s))'
    cursor.execute(query, (text, date))
    connection.commit()
    connection.close()


def return_text_for_history():
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='Mshrmwllpsnu1',
        database='words'
    )
    cursor = connection.cursor()
    query = 'SELECT history_text, date FROM words.history WHERE history_text <> "";'
    cursor.execute(query)
    ls = []
    for row in cursor.fetchall():
        ls.append(row)  # get list with tuples [(text,date),....,(text,date)]
    connection.close()
    return ls


def cast_verbs(word):  # return 3 or 4 words
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='Mshrmwllpsnu1',
        database='words'
    )
    try:
        ls = []
        cursor = connection.cursor(buffered=True)
        query = 'SELECT choice1,choice2,choice3 FROM words.irregular_words WHERE choice1 =%s OR choice2= %s OR choice3 = %s OR additional_choice = %s LIMIT 1;'
        cursor.execute(query, (word,word,word,word))
        for row in cursor.fetchall():
            ls.append(row)
        return (' '.join(*ls))  # get list  word word word
    except TypeError:
        try:
            query2 = 'SELECT choice1,choice2,choice3,choice4 FROM words.regular_verbs WHERE choice1 = %s OR choice2= %s OR choice3 = %s OR choice4 = %s LIMIT 1;'
            cursor.execute(query2, (word, word, word,word))
            for row in cursor.fetchall():
                ls.append(row)  # get list with tuples [(text,date),....,(text,date)]
            return (' '.join(*ls))
        except TypeError:
            return False