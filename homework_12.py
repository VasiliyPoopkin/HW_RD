#task 1


import json
#
# phone_book_file = "phone_book.json"
# phone_book = {}
#
# def add_contact(name, phone):
#     phone_book[name] = phone
#
#
# def save_phone_book(phone_book):
#     with open("phone_book.json", "w") as json_file:
#         json.dump(phone_book, json_file)
#
#
# def load_phone_book():
#     global phone_book
#     try:
#         with open('phone_book.json', 'r') as f:
#             phone_book = json.load(f)
#     except FileNotFoundError:
#         print('Файл з телефонною книгою не знайдено. Створено нову телефонну книгу.')
#
#
# def stats():
#     print("Кількість записів: {}".format(len(phone_book)))
#
#
# def add():
#     name = input("Введіть ім'я: ")
#     phone_number = input("Введіть номер телефону: ")
#     phone_book.update({name:phone_number})
#     print("Запис додано")
#
#
# def delete(name):
#     if name in phone_book:
#         del phone_book[name]
#         print("Запис видалено")
#     else:
#         print("Запис з іменем {} не знайдено".format(name))
#
#
# def list_names():
#     print("Контакти:")
#     for name in phone_book:
#         print(name)
#
#
# def show():
#     load_phone_book()
#     if name in phone_book:
#         print("Ім'я: {}".format(name))
#         print("Номер телефону: {}".format(phone_book[name]))
#     else:
#         print("Запис з іменем {} не знайдено".format(name))
#
#
# while True:
#     print("\n Введіть команду: Контакти, Додати, Видалити <name>, Список, Показати <name>, або Вихід")
#     command = input()
#     if command == "Контакти":
#         stats()
#     elif command == "Додати":
#         add()
#     elif command.startswith("Видалити "):
#         name = command.split()[1]
#         delete(name)
#     elif command == "Список":
#         list_names()
#     elif command.startswith("Показати "):
#         name = command.split()[1]
#         show(name)
#     elif command == "Вихід":
#         save_phone_book(phone_book)
#         break
#     else:
#         print("Невідома команда")


#task 2


# import datetime
#
# def print_call_info(times):
#     def wrapper(func):
#         def inner(*args, **kwargs):
#             logs = {}
#             for i in range(times):
#                 print(f'Function name: {func.__name__}')
#                 print(f'Time: {datetime.datetime.now()}')
#                 result = func(*args, **kwargs)
#                 logs.update({times:[func.__name__, datetime.datetime.now()]})
#             with open("logs.json", "w") as json_file:
#                 json.dump(json.dumps(logs, default=str), json_file)
#             return result
#         return inner
#     return wrapper
#
#
# @print_call_info(times=1)
#
# def sum_number(a, b):
#     return a + b
#
# result = sum_number(2, 2)
# print(result)


#task 3


# class ContextManager:
#     def __enter__(self):
#         print("==========")
#
#     def __exit__(self, exc_type, exc_value, traceback):
#         print("==========")
#         if exc_type is not None:
#             print(f"An error occurred: {exc_type.__name__}: {exc_value}")
#             with open("logs.txt", "a") as file:
#                 file.write(f"{exc_type.__name__}: {exc_value}")
#         return True
#
# with ContextManager():
#     def sum_number(a, b):
#         return a + b
#     result = sum_number(2, 2)
#     print(result)
