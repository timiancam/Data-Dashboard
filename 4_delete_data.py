"""
Deletes data from the fortune_500_table
"""

import connection_handler as ch

try:
    ch.CUR.execute("DELETE FROM fortune_500_table WHERE name = 'Timothy_Cameron';")
    print('Data deleted from table\n')
except ch.ps2.Error as e:
    print('Error deleting data from table\n')
    print(e)

ch.database_disconnect()
