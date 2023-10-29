"""
Deletes SQL tables
"""

import connection_handler as ch

try:
    ch.CUR.execute('DROP TABLE fortune_500_table;')
    print('fortune_500_table table deleted\n')
except ch.ps2.Error as e:
    print('Error deleting fortune_500_table\n')
    print(e)
ch.database_disconnect()
