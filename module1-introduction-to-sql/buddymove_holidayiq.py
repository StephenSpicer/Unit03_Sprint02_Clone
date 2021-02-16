""" Making a database from the buddymove csv"""

import pandas as pd
import sqlite3

df_buddymove = pd.read_csv('buddymove_holidayiq.csv')


conn = sqlite3.connect('buddymove_holidayiq.sqlite3')
conn

curs = conn.cursor()
curs

df_buddymove.to_sql('buddymove_holidayiq', con=conn)



""" BuddyMove Queries """

# Count how many rows you have - it should be 249!
row_count ="""
SELECT COUNT(*)
FROM buddymove_holidayiq
"""

# How many users who reviewed at least 100 `Nature`
# in the category also reviewed at least 100 in the `Shopping` category?

user_count100 = """
SELECT COUNT(*)
FROM buddymove_holidayiq
WHERE Nature > 100 AND Shopping > 100
"""



# - (*Stretch*) 
# What are the average number of reviews for each category?
# Sports, Religious, Theatre, Shopping, Nature, Picnic
avg_per_category ="""
SELECT AVG(totreviews)
FROM (SELECT SUM())
"""

#OK, wasted a lot of time researching that with no solution.
#Learned a lot, will return when it's easier with the new SQL material.
# Goodnight for now... 