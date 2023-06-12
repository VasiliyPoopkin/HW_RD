phone_book = {}

def stats():
    print("Кількість записів: {}".format(len(phone_book)))

def add():
    name = input("Введіть ім'я: ")
    phone_number = input("Введіть номер телефону: ")
    phone_book[name] = phone_number
    print("Запис додано")

def delete(name):
    if name in phone_book:
        del phone_book[name]
        print("Запис видалено")
    else:
        print("Запис з іменем {} не знайдено".format(name))

def list_names():
    print("Контакти:")
    for name in phone_book:
        print(name)

def show(name):
    if name in phone_book:
        print("Ім'я: {}".format(name))
        print("Номер телефону: {}".format(phone_book[name]))
    else:
        print("Запис з іменем {} не знайдено".format(name))


while True:
    print("\n Введіть команду: Контакти, Додати, Видалити <name>, Список, Показати <name>, або Вихід")
    command = input()
    if command == "Контакти":
        stats()
    elif command == "Додати":
        add()
    elif command.startswith("Видалити "):
        name = command.split()[1]
        delete(name)
    elif command == "Список":
        list_names()
    elif command.startswith("Показати "):
        name = command.split()[1]
        show(name)
    elif command == "Вихід":
        break
    else:
        print("Невідома команда")