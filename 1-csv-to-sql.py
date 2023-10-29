"""
Creates SQL database from a .csv file
"""

import pandas as pd
import connection_handler as ch

df = pd.read_csv('fortune_500_companies.csv')

try:
    df.to_sql('fortune_500_table', ch.ENGINE)
    print('SQL table created and .csv data inserted\n')
except ValueError as e:
    print('Error converting dataframe to SQL table\n')
    print(e)
ch.database_disconnect()
