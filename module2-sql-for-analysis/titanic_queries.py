""" list of queries / statements to get our titanic tables set up on postgres """

SELECT_ALL = """
  SELECT * FROM {};
  """

create_titanic_table = """
  CREATE TABLE titanic_disaster (
    index_id SERIAL PRIMARY KEY,
    Survived INT,
    Pclass INT,
    Name VARCHAR(100),
    Sex VARCHAR(10),
    Age INT,
    SiblingsSpouses INT,
    ParentsChildren INT,
    Fare INT
  );
"""