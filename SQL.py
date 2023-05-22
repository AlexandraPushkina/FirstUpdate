import mysql.connector
from mysql.connector import Error
from enum import Enum
# theme = Enum('theme',['Nature','Technology','Social'])

def get_text(theme):  #connection and query for database
    connection = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = 'Mshrmwllpsnu1',
            database = 'words'
        )
    cursor = connection.cursor()
    query = 'SELECT text FROM words.text_collections WHERE theme = %s'  #query with parametr
    cursor.execute(query, (theme, ))
    for row in cursor.fetchall():   #for check
        print(row)

def save_in_history(text):
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='Mshrmwllpsnu1',
        database='words'
    )
    cursor = connection.cursor()
    query = 'INSERT INTO words.history(history_text) VALUES (%s)'
    cursor.execute(query,(text, ))
    connection.commit()

