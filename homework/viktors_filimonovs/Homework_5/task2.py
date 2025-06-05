def process_result(text):
    colon_index = text.index(":")
    number = int(text[colon_index + 1:].strip())
    # print(f"Результат сложения: {number + 10}")
    print(f"{text[:colon_index]}: {number + 10}")


texts = [
    "результат операции: 42",
    "результат операции: 514",
    "результат работы программы: 9"
]


for text in texts:
    process_result(text)
