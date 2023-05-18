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
    query = 'SELECT text FROM words.text_collections WHERE theme = %s'
    cursor.execute(query, (theme, ))
    for row in cursor.fetchall():
        print(row)

# get_text(tuple('Nature'))
get_text('Nature')