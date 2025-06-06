import random

secret_number = random.randint(0, 9)
# print(secret_number)

while True:
    user_enter = int(input("Guess the number from 0-9: "))
    if user_enter == secret_number:
        print("whoop u win!")
        break
    else:
        print("Guess again!")
