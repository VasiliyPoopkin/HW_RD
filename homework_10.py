#task 1


# phone_book = {}
#
# def stats():
#     print("Кількість записів: {}".format(len(phone_book)))
#
# def add():
#     name = input("Введіть ім'я: ")
#     try:
#         phone_number = str(input("Введіть номер телефону: "))
#         if len(phone_number) < 11:
#             print("Ви ввели не вірний номер")
#         elif len(phone_number) == 11:
#             phone_book[name] = phone_number
#             print("Запис додано")
#     except ValueError:
#         print("Помилка")
#
#
# def delete(name):
#     if name in phone_book:
#         del phone_book[name]
#         print("Запис видалено")
#     else:
#         print("Запис з іменем {} не знайдено".format(name))
#
# def list_names():
#     print("Контакти:")
#     for name in phone_book:
#         print(name)
#
# def show(name):
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
#         try:
#             command = int("Контакти")
#             print("Невідома команда")
#         except ValueError:
#             stats()
#     elif command == "Додати":
#         try:
#             command = int("Додати")
#             print("Невідома команда")
#         except ValueError:
#             add()
#     elif command.startswith("Видалити "):
#         try:
#             command = int("Видалити")
#             print("Невідома команда")
#         except ValueError:
#             name = command.split()[1]
#             delete(name)
#     elif command == "Список":
#         try:
#             command = int("Список")
#             print("Невідома команда")
#         except ValueError:
#             list_names()
#     elif command.startswith("Показати "):
#         try:
#             command = int("Контакти")
#             print("Невідома команда")
#         except ValueError:
#             name = command.split()[1]
#             show(name)
#     elif command == "Вихід":
#         try:
#             command = int("Вихід")
#             print("Невідома команда")
#         except ValueError:
#             break
#     else:
#         print("Невідома команда")


#task 2

# class DemoException(Exception):
#     def __init__(self, message, error_code):
#         super().__init__(message)
#         self.error_code = error_code
#     def get_error_code(self):
#         return self.error_code
#
# try:
#     raise DemoException
# except DemoException as e:
#     print("Custom exception is occurred")
