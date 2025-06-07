import random


salary = int(input('What is your salary?: '))
bonus = random.choice([True, False])
bonus_amount = random.randint(100, 500) if bonus else 0
total_salary = salary + bonus_amount


print(f"{salary}, {bonus} - '${total_salary}")
