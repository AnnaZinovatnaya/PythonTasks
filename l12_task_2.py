from contextlib import contextmanager
from datetime import datetime


@contextmanager
def timer():
    start_time = datetime.now()
    try:
        yield
    finally:
        elapsed_time = datetime.now() - start_time
        print(f'Elapsed time: {elapsed_time}')


with timer():
    val = 0
    for _ in range(100000000):
        val += 10
