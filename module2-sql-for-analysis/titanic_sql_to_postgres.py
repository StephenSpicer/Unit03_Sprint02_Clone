""" sending our titanic data from sql to postgres """

import sqlite3
import psycopg2
import titanic_queries as q 

DBNAME = "hqpmzrvd"
USER = "hqpmzrvd"
PASSWORD = "R2T6PlWnH5qYUwS67lMtNpk7Ry1UJVRo"
HOST = "ziggy.db.elephantsql.com"

sqlite_titanic_db = "titanic_to_sql.sqlite3"

# connection

def sqlite_connect(sqlite_titanic_db):
    """ returns sqlite connections """
    sqlite_conn = sqlite3.connect(sqlite_titanic_db)
    return sqlite_conn

def pg_connect(dbname, password, user, host):
    """ returns pg connection object """
    pg_conn = psycopg2.connect(dbname=DBNAME, user=USER, password=PASSWORD, host=HOST)
    return pg_conn

# cursor

def create_cursor(conn):
    """ returns cursor """
    curs = conn.cursor()
    return curs

def execute_query(curs, query, reading=True):
    """ executes query """
    curs.execute(query)
    if reading:
        results = curs.fetchall()
        return results

def add_titanic(pg_curs, passenger_list):
    """Grabbing characters from sqlite"""
    passenger_list_temp = """
      INSERT INTO titanic_disaster
      (index_id, Survived, Pclass, Name, Sex, Age, SiblingsSpouses, ParentsChildren, Fare)
      VALUES {};
    """
    for passenger in passenger_list:
        pg_curs.execute(passenger_list_temp.format(passenger))


if __name__ == "__main__":
    pg_conn = pg_connect(DBNAME, USER, PASSWORD, HOST)
    pg_curs = create_cursor(pg_conn)
    

    sl_conn = sqlite_connect(sqlite_titanic_db)
    sl_curs = create_cursor(sl_conn)

    results = execute_query(pg_curs, q.create_titanic_table, reading=False)

    passenger_list = execute_query(sl_curs, q.SELECT_ALL.format("titanic"))
    
    add_titanic(pg_curs, passenger_list)

    pg_conn.commit()
    sl_conn.commit()