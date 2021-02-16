""" A pipeline that transfers data from sqlite to postgreSQL """

import psycopg2
import queries as q 


dbname = "isgyfdvp"
user = "isgyfdvp"
password = "yNfvRPtWgSQUdB0YIu1kO-PiPcnSGgAe"
host = "ziggy.db.elephantsql.com"

# Make connection
def pg_connect(dbname, password, user, host):
    """ returns pg connection object """
    pg_conn = psycopg2.connect(dbname=dbname, user=user,
                           password=password, host=host)
    return pg_conn

# Make Cursor
def create_cursor(conn):
    """ returns cursor """
    curs = conn.cursor()
    return curs

# Making our query

def execute_query(curs, query):
    """ executes query """
    curs.execute(query)
    results = curs.fetchall()
    return results

if __name__ == "__main__":
    pg_conn = pg_connect(DBNAME, USER, PASSWORD, HOST)
    pg_curs = create_cursor(pg_conn)
    results = execute_query(pg_curs, q.CREATE_TEST_TABLE_STATEMENT)
    results2 = execute_query(pg_curs, q.TEST_INSERT_STATEMENT)

    all_data = execute_query(pg_curs, q.SELECT_ALL.format("TEST_TABLE"))