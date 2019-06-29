from datetime import datetime


class timer:
    def __enter__(self):
        self.start_time = datetime.now()

    def __exit__(self, exc_type, exc_value, exc_traceback):
        elapsed_time = datetime.now() - self.start_time
        print(f'Elapsed time: {elapsed_time}\n')
        return True

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            start_time = datetime.now()
            ret_val = func(*args, **kwargs)
            elapsed_time = datetime.now() - start_time
            print(f'Elapsed time: {elapsed_time}\n')
            return ret_val

        return wrapper

with timer():
    print('inside context manager with exception')
    a = 10
    b = 0
    try:
        x = a / b
    except ZeroDivisionError:
        print('You cannot divide by zero')

with timer():
    print('inside context manager with if')
    a = 10
    b = 0
    if b != 0:
        x = a / b
    else:
        print('You cannot divide by zero')


@timer()
def divide_with_exception(a, b):
    print(f'divide_with_exception({a}, {b})')
    try:
        return a / b
    except ZeroDivisionError:
        print('You cannot divide by zero')
        return 0


@timer()
def divide_with_if(a, b):
    print(f'divide_with_if({a}, {b})')
    if b != 0:
        return a / b
    else:
        print('You cannot divide by zero')
        return 0


divide_with_exception(10, 0)
divide_with_if(10, 0)
