"""
Reads data from SQL database
"""

import connection_handler as ch

try:
    ch.CUR.execute("SELECT * FROM fortune_500_table WHERE name = 'Timothy_Cameron';")
    print('Data has been selected\n')
    
    ROW = ch.CUR.fetchone()
    
    while ROW:
        print(ROW)
        ROW = ch.CUR.fetchone()
        
except ch.ps2.Error as e:
    print('Error selecting data\n')
    print(e)

ch.database_disconnect()
