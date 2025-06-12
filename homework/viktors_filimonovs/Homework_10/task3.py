from functools import wraps


def operation_controller(func):
    @wraps(func)
    def wrapper(first, second):
        if first == 0 and second == 0:
            return "Devide to 0 error"
        if first < 0 or second < 0:
            operation = "*"
        elif first == second:
            operation = "+"
        elif first > second:
            operation = "-"
        elif second > first:
            operation = "/"
        else:
            raise ValueError("Unexpected situation5")

        return func(first, second, operation)

    return wrapper


@operation_controller
def calc(first, second, operation):
    if operation == '+':
        return first + second
    elif operation == '-':
        return first - second
    elif operation == '/':
        return first / second
    elif operation == '*':
        return first * second
    else:
        return "Wrong operation"


first_number = float(input("Введите первое число: "))
second_number = float(input("Введите второе число: "))

result = calc(first_number, second_number)
print(f"Результат: {result}")
