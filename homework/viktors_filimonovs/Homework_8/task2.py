import sys
sys.set_int_max_str_digits(100000)


def la_fibanachi_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


fib_gen = la_fibanachi_generator()


positions = [5, 200, 1000, 100000]
for pos in positions:
    for _ in range(pos - 1):
        next(fib_gen)
    print(f"{pos}-e fibbanachi letter:", next(fib_gen))
