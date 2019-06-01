import time
import functools


def my_lru_decorator(maxsize):
    def decorator(func):
        history = {}  # {(number, result): timestamp}

        @functools.wraps(func)
        def wrapper(number):
            ret = None
            for val in history.keys():
                if val[0] == number:
                    print('<return from history>')
                    ret = val[1]
                    break
            else:
                print('<calculate>')
                ret = func(number)
                if len(history) == maxsize:
                    print('<reached max size>')
                    history.pop(min(history.keys(), key=history.get))
                history[(number, ret)] = time.time()
            return ret
        return wrapper
    return decorator


@my_lru_decorator(5)
def my_power_three(number):
    """ Raise any number to a power of three
    """
    return number ** 3


print('Result = {}\n'.format(my_power_three(1)))
print('Result = {}\n'.format(my_power_three(2)))
print('Result = {}\n'.format(my_power_three(3)))
print('Result = {}\n'.format(my_power_three(4)))
print('Result = {}\n'.format(my_power_three(5)))
print('Result = {}\n'.format(my_power_three(6)))
print('Result = {}\n'.format(my_power_three(5)))
