import sqlite3

con = sqlite3.connect(
    "/Users/hiraharatetsuya/Downloads/python_Lecture/database/sample.db")
cursor = con.cursor()


target_name = input("whose 'age' do you want to update?:")
new_age = input("Tell me new age :")
print(target_name, new_age)
update_query = f"UPDATE User SET age = {new_age}WHERE name = '{target_name}'"
cursor.executescript(update_query)
