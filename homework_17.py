import sqlite3

#task 1

# conn = sqlite3.connect("C:/Users/Turbo/Downloads/646b6d1be99f9535870886.sqlite")
# cursor = conn.cursor()
#
# # query = "SELECT * FROM users WHERE age > 30"
# cursor.execute("SELECT * FROM users WHERE age > 30")
#
# results = cursor.fetchall()
# for row in results:
#     print(row)
#
# conn.close()


#task 2


# conn = sqlite3.connect("C:/Users/Turbo/Downloads/646b6d1be99f9535870886.sqlite")
# cursor = conn.cursor()
#
# query = "SELECT COUNT(*) FROM users WHERE age > 30"
# cursor.execute(query)
#
# count = cursor.fetchone()[0]
#
# print("Кількість записів старше 30 років:", count)
# conn.close()

#task 3


# conn = sqlite3.connect("C:/Users/Turbo/Downloads/646b6d1be99f9535870886.sqlite")
# cursor = conn.cursor()
#
# query = ("SELECT age, COUNT(*) FROM users ("
#          "FROM users "
#          "GROUP BY age )")
#
# cursor.execute(query)
# results = cursor.fetchall()
#
# print("age  | users")
# print("------|-------")
# for row in results:
#     print(f"{row[0]:4}  | {row[1]}")
#
# conn.close()


#task 4


# conn = sqlite3.connect("C:/Users/Turbo/Downloads/646b6d1be99f9535870886.sqlite")
# cursor = conn.cursor()
#
# query = ("SELECT age, COUNT(*) AS user_count "
#          "FROM users "
#          "GROUP BY age "
#          "ORDER BY user_count DESC, age ASC")
#
# results = cursor.fetchall()
#
# print("age  | users")
# print("------|-------")
# for row in results:
#     print(f"{row[0]:4}  | {row[1]}")
#
# conn.close()


#task 5


# conn = sqlite3.connect("C:/Users/Turbo/Downloads/646b6d1be99f9535870886.sqlite")
# cursor = conn.cursor()
#
# query = ("SELECT age, users FROM ("
#          "SELECT age, COUNT(*) AS users "
#          "FROM users "
#          "GROUP BY age "
#          "HAVING users > 1 "
#          "ORDER BY users DESC, age ASC ")
#
# cursor.execute(query)
#
# results = cursor.fetchall()
#
# print("age  | users")
# print("------|-------")
# for row in results:
#     print(f"{row[0]:4}  | {row[1]}")
#
# conn.close()






