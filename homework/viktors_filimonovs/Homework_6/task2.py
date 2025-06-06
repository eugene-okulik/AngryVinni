import heapq


def fuzBuz():
    for number in range(1, 101):
        if number % 3 == 0 and number % 5 == 0:
            print("FuxzBuzz")
        elif number % 3 == 0:
            print("Fuzz")
        elif number % 5 == 0:
            print("Buzz")
        else:
            print(number)


def fuzBuzz():
    for number in range(1, 101):
        result = ("Fuzz" * (number % 3 == 0)) + ("Buzz" * (number % 5 == 0))
        print(result or number)


def fizzbuzz(n):
    heap = list(range(1, n + 1))
    heapq.heapify(heap)

    while heap:
        i = heapq.heappop(heap)
        result = ('Fizz' * (i % 3 == 0) + 'Buzz' * (i % 5 == 0)) or str(i)
        print(result)


fuzBuz()

print('=' * 30)

fuzBuzz()

print('=' * 30)

fizzbuzz(258)
