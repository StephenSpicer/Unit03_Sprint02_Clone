""" These will be our northwind sql setup and queries """
import sqlite3


conn = sqlite3.connect('Northwind_small.sqlite')
curs = conn.cursor()


# connection execute
def execute_q(conn, query):
    curs = conn.cursor()
    curs.execute(query)
    results = curs.fetchall()
    curs.close()
    return results


# 10 most expensive:


def expensive_items():
    items = """
    SELECT *
    FROM Product
    ORDER BY
            UnitPrice DESC
    LIMIT 10;
    """
    return items


# average hire age:
def avg_hire_age():
    avg_age = """
    SELECT AVG(Hiredate - Birthdate)
    FROM Employee
    """
    return avg_age


# 10 most expensive with supplier included:
def ten_most_expensive():
    items_supp = """
    SELECT CompanyName, ProductName
    FROM Supplier
    INNER JOIN Product
    ON Product.SupplierId = Supplier.Id
    ORDER BY
            UnitPrice DESC
    LIMIT 10;
    """
    return items_supp


def largest_category():
    large_c = """
    SELECT DISTINCT CategoryId, CategoryName
    FROM Product, Category
    WHERE Category.Id = Product.CategoryId
    GROUP BY CategoryId
    ORDER BY COUNT(*) DESC LIMIT 1;
"""
    return large_c

ten_most_exp = execute_q(conn, expensive_items())
print("10 most expensive: ", ten_most_exp)

print()
avg_at_hire = execute_q(conn, avg_hire_age())
aah = [i[0] for i in avg_at_hire]
print("average age at time of hire: ", str(round(aah[0], 2)))
print()
print()
exp_and_supplier = execute_q(conn, ten_most_expensive())
print("ten most expensive items and suppliers: ", exp_and_supplier)
print()
largest_cat = execute_q(conn, largest_category())
print("largest category ID and Name: ", largest_cat)
