""" Queries for sqlite to PostGreSQL pipeline """
# REMEMBER THIS IS POSTGRES DIALECT - SO INT RATHER THAN INTEGER, SO ON AND SO FORTH...
# table_info = "PRAGMA table_info(charactercreator_character);"

SELECT_ALL = """
  SELECT * FROM {};
  """


create_character_table = """
  CREATE TABLE IF NOT EXISTS charactercreator_character (
    character_id SERIAL PRIMARY KEY,
    name VARCHAR(30),
    level INT,
    exp INT,
    hp INT,
    strength INT,
    intelligence INT,
    dexterity INT,
    wisdom INT
  );
"""

INSERT_STATEMENT = """
   INSERT INTO charactercreator_character(
    character_id,
    name,
    level,
    exp,
    hp,
    strength,
    intelligence,
    dexterity,
    wisdom
   ) VALUES {};
"""


# CREATE_TEST_TABLE_STATEMENT = """
#   CREATE TABLE IF NOT EXISTS test_table (
#     id SERIAL PRIMARY KEY,
#     name varchar(20),
#     age INT
#   );
# """

# double quotes in postgres get taken as column... so use single for input.

