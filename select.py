import sqlite3

con = sqlite3.connect(
    "/Users/hiraharatetsuya/Downloads/python_Lecture/database/sample.db")
cursor = con.cursor()
for rew in cursor.execute("SELECT * FROM [Album]"):
    print(rew)


# print(next(cursor))
# print(next(cursor))
# print(next(cursor))
# print(cursor.fetchall())
