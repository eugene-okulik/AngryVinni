def process_result(text):
    number = int(text.split(":")[1].strip())
    return f"{text.split(':')[0]}: {number + 10}"


texts = [
    "результат операции: 42",
    "результат операции: 54",
    "результат работы программы: 209",
    "результат: 2"
]

for text in texts:
    print(process_result(text))
