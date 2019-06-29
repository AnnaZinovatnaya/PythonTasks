import datetime


class timer(object):
    def __enter__(self):
        self.start_time = datetime.datetime.now()

    def __exit__(self, exc_type, exc_value, exc_traceback):
        elapsed_time = datetime.datetime.now() - self.start_time
        print(f'Elapsed time: {elapsed_time}')
        return True


with timer():
    sum = 0
    for i in range(10000000):
        sum += i
