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
    for row in cursor.fetchall():  # for check
        ls.append(row)  # get list with tuples [(text,date),....,(text,date)]
    connection.close()
    return ls


def cast_verbs(word):  # not worked!
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='Mshrmwllpsnu1',
        database='words'
    )
    cursor = connection.cursor()
    query = 'SELECT'
