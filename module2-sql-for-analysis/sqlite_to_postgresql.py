""" A pipeline that transfers data from sqlite to postgreSQL """

import sqlite3
import psycopg2
import queries as q 


DBNAME = "czlilzkt"
USER = "czlilzkt"
PASSWORD = "4tYRkcFoQmWeqSlgHGr_1ZGisox4BKBI"
HOST = "ziggy.db.elephantsql.com"

sqlite_rpg_db = "rpg_db.sqlite3"

# Make connection_______
# sqlite connector
def sqlite_connect(sqlite_db):
    """ returns sqlite connections """
    sqlite_conn = sqlite3.connect(sqlite_db)
    return sqlite_conn

#postgres connector
def pg_connect(dbname, password, user, host):
    """ returns pg connection object """
    pg_conn = psycopg2.connect(dbname=DBNAME, user=USER, password=PASSWORD, host=HOST)
    return pg_conn

# Make Cursor______
def create_cursor(conn):
    """ returns cursor """
    curs = conn.cursor()
    return curs

# Making our query

def execute_query(curs, query, reading=True):
    """ executes query """
    curs.execute(query)
    if reading:
        results = curs.fetchall()
        return results


# OK, this is nicks code for adding characters. it runs through a for loop below for each character in the list. 
def add_characters(pg_curs, character_list):
    """Grabbing characters from sqlite"""
    insert_character_statement = """
      INSERT INTO charactercreator_character
      (character_id, name, level, exp, hp, strength, intelligence, dexterity, wisdom)
      VALUES {};
    """
    for character in character_list:
        pg_curs.execute(insert_character_statement.format(character))

# THE IF NAME MAIN SECTION ________

if __name__ == "__main__":
    pg_conn = pg_connect(DBNAME, USER, PASSWORD, HOST)
    pg_curs = create_cursor(pg_conn)
    

    sl_conn = sqlite_connect(sqlite_rpg_db)
    sl_curs = create_cursor(sl_conn)


    
    

    # all_data = execute_query(pg_curs, q.SELECT_ALL.format("TEST_TABLE"))
    
    results = execute_query(pg_curs, q.create_character_table, reading=False)
    character_list = execute_query(sl_curs, q.SELECT_ALL.format("charactercreator_character"))
    add_characters(pg_curs, character_list)

    pg_conn.commit()
    sl_conn.commit()

    print(character_list)