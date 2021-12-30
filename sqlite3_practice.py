import sqlite3

con = sqlite3.connect("database/sample.db")
print(con)
cursor = con.cursor()
print(cursor)

create_user_table_query = """
CREATE TABLE IF NOT EXISTS User (
  UserId INTEGER PRIMARY KEY NOT NULL,
  Name TEXT DEFAULT 'anoymous',
  Email TEXT NOT NULL,
  Age INTEGER CHECK(age > 0 ))
"""
cursor.execute(create_user_table_query)

insert_user_query = """
INSERT INTO User VALUES(1, 'john', 'john@gamil.com', 30);
INSERT INTO User VALUES(2, 'john1', 'john1@gamil.com', 33);
INSERT INTO User VALUES(3, 'john2', 'john2@gamil.com', 34);
"""
cursor.executescript(insert_user_query)
con.commit()
