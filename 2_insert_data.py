"""
Inserts data into the fortune_500_table
"""

import connection_handler as ch

SQL_STATEMENT = """INSERT INTO fortune_500_table(name, rank, year, industry, sector, headquarters_state, headquarters_city, market_value_mil, revenue_mil, profit_mil, asset_mil, employees, founder_is_ceo, female_ceo, newcomer_to_fortune_500, global_500)
VALUES('Timothy_Cameron', '1', '2023', 'Engineering', 'Engineering', 'MI', 'Detroit', '1', '1', '1', '1', '1', 'yes', 'no', 'no', 'yes');"""

try:
    ch.CUR.execute(SQL_STATEMENT)
    print('Data sucessfully inserted into table.\n')
except ch.ps2.Error as e:
    print('Data unsuccesfully inserted into table, try again!\n')
    print(e)

ch.database_disconnect()
