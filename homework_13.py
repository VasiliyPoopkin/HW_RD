#task 1


# import json
# import re
#
#
# phone_book_file = "phone_book.json"
# phone_book = {}
# PATTERN  = re.compile(r'^(?:\+38|38|0)?\d{9,10}$')
# def add_contact(name, phone):
#     phone_book[name] = phone
#
#
# def save_phone_book(phone_book):
#     with open("phone_book.json", "a") as json_file:
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
#     if re.match(PATTERN, phone_number):
#         phone_book[name] = phone_number
#         print("Запис додано")
#     else:
#         print("Номер телефону не вірний!")
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


# import sys
#
#
# if len(sys.argv) != 2:
#     print("Використання: python програма.py <назва_файлу>")
#     sys.exit(1)
# filename = sys.argv[1]
#
# with open(filename, 'r') as f:
#     text = f.read()
#
# email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
# text = re.sub(email_pattern, '*@*', text)
#
#
# print(text)


#task 3


# file_name = input("Введіть ім'я файлу: ")
#
# with open(file_name, 'r') as f:
#     text = f.read()
#
# email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
# emails = re.findall(email_pattern, text)
#
# for email in emails:
#     first_char = email[0]
#     last_char = email[-1]
#     replacement = f'X{("*" * (len(email)-2))}X'
#     text = text.replace(email, f'{first_char}{replacement}{last_char}')
#
# with open(file_name, 'w') as f:
#     f.write(text)
#
# print("Усі email-адреси в зазначеному файлі були замінені на X***@****X.")