""" list of queries / statements to get our titanic tables set up on postgres """

create_titanic_table = """
  CREATE TABLE IF NOT EXISTS titanic_disaster (
    index_id SERIAL PRIMARY KEY,
    Survived INT,
    Pclass INT,
    name VARCHAR(60),
    Sex VARCHAR(10),
    Age INT,
    Siblings/Spouses Aboard INT,
    Parents/Children Aboard INT,
    Fare INT
  );
"""