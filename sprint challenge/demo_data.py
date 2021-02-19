""" queries for the demo data sqlite database """

import sqlite3


conn = sqlite3.connect('demo_data.sqlite3')
curs = conn.cursor()


def execute_q(conn, query):
    curs = conn.cursor()
    curs.execute(query)
    results = curs.fetchall()
    curs.close()
    return results


def make_table():
    query = """
    CREATE TABLE data (
        s CHAR(1),
        x INT,
        y INT
    );
    """
    return query


def clear_table():
    query = """
    DROP TABLE data;
    """
    return query


def insert_statement():
    query = """
    INSERT INTO data (s, x, y)
    VALUES
    ('g', 3, 9),
    ('v', 5, 7),
    ('f', 8, 7);
    """
    return query

# Now that we've got that up lets type those queries:


def row_count():
    row_count = """
    SELECT COUNT(s)
    FROM data;
    """
    return row_count


def xy_at_least_5():
    xycount = """
    SELECT x, y
    FROM data
    WHERE x >= 5
    AND y >= 5;
    """
    return xycount


def unique_y():
    yunique = """
    SELECT COUNT(DISTINCT y)
    FROM data;
    """
    return yunique

execute_q(conn, clear_table())

execute_q(conn, make_table())

execute_q(conn, insert_statement())

rc = execute_q(conn, row_count())
rcp = [i[0] for i in rc]
print("row count =:", rcp)

xy5 = execute_q(conn, xy_at_least_5())
print("x and y >= 5: ", xy5)

yd = execute_q(conn, unique_y())
print("distinct y count: ", yd)


conn.commit()
