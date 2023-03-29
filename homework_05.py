# task 1

while True:
    user_input = input("Write down your data: ")
    for char in user_input:
        if char.isalpha():
            if char.isupper():
                letter_case = "Capital"
            else:
                letter_case = "small"
            print(f"it's a letter {letter_case} {char}")
        elif char.isdigit():
            if int(char) % 2 == 0:
                parity = "paired"
            else:
                parity = "unpaired"
            print(f"It's a number {parity} {char}")
        else:
            print("it's a symbol", char)

#task 2

import time

while True:
    print("I love Python")
    time.sleep(4.2)


# task 3

for i in range(1, 6):
    for j in range(1, i+1):
        print(j, end=" ")
    print()