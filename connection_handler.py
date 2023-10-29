"""
Handles connections to the postgres database 
Creates fortune_500_table
Creates global connection, cursor and engine variables
Accessed by other modules
"""

import psycopg2 as ps2
from sqlalchemy import create_engine

# connect to the database
try:
    ENGINE = create_engine('postgresql+psycopg2://::@localhost:5432/postgres')
    CONN = ENGINE.raw_connection()
    CONN.set_session(autocommit=True)
    CUR = CONN.cursor()
except ps2.Error as e:
    print('Error connecting to database.')
    print(e)

def database_disconnect():
    CUR.close()
    CONN.close()
    print('Disconnected from database.\n')
