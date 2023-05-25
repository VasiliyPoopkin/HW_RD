#task 1

import sqlite3


# connection = sqlite3.connect("D:\HW_RD\identifier.sqlite")
# cursor = connection.cursor()
#
# query = ("CREATE TABLE IF NOT EXISTS users ("
#          "id INTEGER PRIMARY KEY AUTOINCREMENT,"
#          "first_name TEXT,"
#          "last_name TEXT,"
#          "age INTEGER)")
#
# connection.commit()
# connection.close()

#task 2


# conn = sqlite3.connect("D:\HW_RD\identifier.sqlite")
# cursor = conn.cursor()
#
#
# cursor.execute("INSERT INTO users (first_name, last_name, age) VALUES ('John', 'Doe', 25)")
#
# cursor.execute("INSERT INTO users (first_name, last_name, age) VALUES ('Jane', 'Smith', 30)")
#
# cursor.execute("INSERT INTO users (first_name, last_name, age) VALUES ('Michael', 'Johnson', 42)")
#
# cursor.execute("INSERT INTO users (first_name, last_name, age) VALUES ('Emily', 'Brown', 28)")
#
# cursor.execute("INSERT INTO users (first_name, last_name, age) VALUES ('William', 'Davis', 35)")
#
#
# conn.commit()
# conn.close()


#task 3


# conn = sqlite3.connect("D:\HW_RD\identifier.sqlite")
# cursor = conn.cursor()
#
# query = ("CREATE TABLE IF NOT EXISTS users ("
#          "id INTEGER PRIMARY KEY AUTOINCREMENT, "
#          "first_name TEXT NOT NULL,"
#          "last_name TEXT NOT NULL, "
#          "age INTEGER)")
#
#
# conn.commit()
# conn.close()


#task 4


# conn = sqlite3.connect("D:\HW_RD\identifier.sqlite")
# cursor = conn.cursor()
#
# query = ("CREATE TABLE IF NOT EXISTS users ("
#          "id INTEGER PRIMARY KEY AUTOINCREMENT, "
#          "first_name TEXT NOT NULL, "
#          "last_name TEXT NOT NULL, "
#          "age INTEGER, "
#          "UNIQUE (first_name, last_name)")

# conn.commit()
# conn.close()

