import sqlite3

#task 1


# conn = sqlite3.connect("D:/HW_RD/book_store.sqlite")
# c = conn.cursor()
#
# c.execute("CREATE TABLE IF NOT EXISTS users ("
#                 "id INTEGER PRIMARY KEY AUTOINCREMENT, "
#                 "first_name TEXT, "
#                 "last_name TEXT, "
#                 "age INTEGER)")
#
# c.execute("CREATE TABLE IF NOT EXISTS publishing_house ("
#                 "id INTEGER PRIMARY KEY AUTOINCREMENT, "
#                  "name TEXT, "
#                  "rating INTEGER DEFAULT 5)")
#
# c.execute("CREATE TABLE IF NOT EXISTS books ("
#                 "id INTEGER PRIMARY KEY AUTOINCREMENT, "
#                 "title TEXT, "
#                 "author TEXT, "
#                 "year INTEGER, "
#                 "price REAL, "
#                 "publishing_house_id INTEGER, "
#                 "FOREIGN KEY (publishing_house_id) REFERENCES publishing_house(id))")
#
# c.execute("CREATE TABLE IF NOT EXISTS purchases ("
#                 "id INTEGER PRIMARY KEY AUTOINCREMENT, "
#                 "user_id INTEGER, "
#                 "book_id INTEGER, "
#                 "date TEXT, "
#                 "FOREIGN KEY (user_id) REFERENCES users(id), "
#                 "FOREIGN KEY (book_id) REFERENCES books(id))")
#
# conn.commit()
# conn.close()


#task 2


# conn = sqlite3.connect("D:/HW_RD/book_store.sqlite")
# c = conn.cursor()
#
# query = '''SELECT purchases.id, purchases.date, users.first_name, users.last_name
#            FROM purchases
#            JOIN users ON purchases.user_id = users.id'''
#
# c.execute(query)
#
# results = c.fetchall()
#
# for row in results:
#     purchase_id, purchase_date, first_name, last_name = row
#     print(f"Purchase ID: {purchase_id}")
#     print(f"Date: {purchase_date}")
#     print(f"User: {first_name} {last_name}")
#     print()
#
# conn.close()|


#task 3


# conn = sqlite3.connect("D:/HW_RD/book_store.sqlite")
# c = conn.cursor()
#
# query = '''SELECT users.id, users.first_name, users.last_name, books.title
#            FROM users
#            JOIN purchases ON users.id = purchases.user_id
#            JOIN books ON purchases.book_id = books.id
#            ORDER BY users.id'''
#
# c.execute(query)
#
# results = c.fetchall()
#
# for row in results:
#     user_id, first_name, last_name, book_title = row
#     print(f"User ID: {user_id}")
#     print(f"Name: {first_name} {last_name}")
#     print(f"Book Title: {book_title}")
#     print()
#
# conn.close()


#task 4


# conn = sqlite3.connect("D:/HW_RD/book_store.sqlite")
# c = conn.cursor()
#
# query = '''SELECT COUNT(*) AS amount
#            FROM purchases
#            JOIN books ON purchases.book_id = books.id
#            WHERE books.author = 'Rowling' '''
#
# c.execute(query)
#
# result = c.fetchone()
#
# amount = result[0]
# print(f"Amount of Purchases for Rowling: {amount}")
#
# conn.close()