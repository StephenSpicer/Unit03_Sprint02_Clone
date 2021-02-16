""" Queries for sqlite to PostGreSQL pipeline """
# REMEMBER THIS IS POSTGRES DIALECT - SO INT RATHER THAN INTEGER, SO ON AND SO FORTH...

SELECT_ALL = """
  SELECT * FROM {};
  """

CREATE_TEST_TABLE_STATEMENT = """
  CREATE TABLE test_table (
    id SERIAL PRIMARY KEY,
    name varchar(20),
    age INT
  );
"""

TEST_INSERT_STATEMENT = """
   INSERT INTO test_table (name, age)
   VALUES 
   (
    "Steven",
    25
   ),
   (
    "Alfred",
    85
   );
"""