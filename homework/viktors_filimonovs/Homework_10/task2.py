from functools import wraps


def repeat_me(func_or_count=None):
    if callable(func_or_count):
        # if the decorator is used without an argument
        @wraps(func_or_count)
        def wrapper(*args, count=1, **kwargs):
            for _ in range(count):
                func_or_count(*args, **kwargs)
        return wrapper
    else:
        # if 'count' argument is passed to the decorator
        def decorator(func):
            @wraps(func)
            def wrapper(*args, **kwargs):
                for _ in range(func_or_count):
                    func(*args, **kwargs)
            return wrapper
        return decorator


# Passing 'count' when function is called
@repeat_me
def example1(text):
    print(text)


example1("print me", count=5)

print('=' * 15)


# passing 'count' into decorator
@repeat_me(1)
def example2(text):
    print(text)


example2("print me")
