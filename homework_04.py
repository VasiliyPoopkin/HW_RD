#task 1

data = input("Write down your data: ")
if data.isdigit():                       #task 2
    if int(data) % 2 == 0:
        print("even")
    else:
        print("odd")
if data.isalpha():                       #task 3
    print(len(data))


#task 4


text = input("Введіть текст: ")

match text:

    case str(x) if x.replace('.', '').isdigit():
        print("Введені дані - число")
    case 'True':
        print("Введені дані - логічне значення")
    case 'False':
        print("Введені дані - логічне значення")
    case _:
        print("Введені дані - рядок")




