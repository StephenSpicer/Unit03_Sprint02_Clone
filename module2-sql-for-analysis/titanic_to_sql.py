""" lets send that titanic csv on over to an sqlite db """

import pandas as pd
import sqlite3

df_titanic = pd.read_csv('titanic.csv')

df_titanic = df_titanic.replace("'", " ", regex=True)


conn = sqlite3.connect('titanic_to_sql.sqlite3')
conn

curs = conn.cursor()
curs

df_titanic.to_sql('titanic', conn)