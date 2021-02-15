""" We Make A Connection : What an Adventure """
import sqlite3
import day01_queries as d1q

# 1: Make a 'conn' object for our DB - RPG char creator!
def connect_to_db=(db_name="rpg_db.sqlite3"):
    return sqlite3.connect(db_name)

# 2 : Make cursor through the conn object
# 3 : (3 is the sql query.py)
# 4 : Execute the query
# 5 : Pull the results

def execute_q(conn, query):
    curs = conn.cursor()
    curs.execute(query)
    results = curs.fetchall()
    curs.close()
    return results

if __name__ =  "__main__":
    conn = connect_to_db()
    results = execute_q(conn, q.select_all)
    print(results[:5)
    print(len(results))
