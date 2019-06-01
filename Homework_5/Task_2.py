import time
import functools
from functools import singledispatch


def timer(func):
    @functools.wraps(func)
    def wrapper(number):
        start_time = time.time()
        res = func(number)
        print('Time = ' + str(time.time() - start_time))
        return res

    return wrapper


def counted(func):
    counter = 0

    @functools.wraps(func)
    def wrapper(number):
        nonlocal counter
        counter += 1
        print('Call ' + str(counter))

        return func(number)

    return wrapper


def cached(func):
    history = {}

    @functools.wraps(func)
    def wrapper(number):
        if number in history.keys():
            print("Return from history")
        else:
            print("Calculate")
            history[number] = func(number)
        return history[number]

    return wrapper


def once(func):
    @functools.wraps(func)
    def wrapper(number):
        if wrapper.was_called:
            print('Function was already called!')
        else:
            res = func(number)
            wrapper.was_called = True
            return res

    wrapper.was_called = False
    return wrapper


@once
def my_power_three(number):
    """ Raise any number to a power of three
    """
    return number ** 3


print('Decorated my_power_three(): name: {}, docstring: {}'.format(my_power_three.__name__,  my_power_three.__doc__))
print(my_power_three(3))
print(my_power_three(4))


@singledispatch
@timer
@counted
@cached
def my_power_two(number, verbose=False):
    """ Raise any number to a power of two
    """
    if verbose:
        print('Some verbose')
    return number ** 2


@my_power_two.register(int)
def _(number, verbose=False):
    if verbose:
        print('got int')
    return number ** 2


@my_power_two.register(float)
def _(number, verbose=False):
    if verbose:
        print('got float')
    return number ** 2


@my_power_two.register(str)
def _(number, verbose=False):
    if verbose:
        print('got str')
    return None


print('Decorated my_power_two(): name: {}, docstring: {}'.format(my_power_two.__name__,  my_power_two.__doc__))
print('Result = {}'.format(my_power_two(1, verbose=True)))
print('Result = {}'.format(my_power_two(4, verbose=True)))
print('Result = {}'.format(my_power_two(6, verbose=True)))
print('Result = {}'.format(my_power_two(1, verbose=True)))
print('Result = {}'.format(my_power_two(1.5, verbose=True)))
print('Result = {}'.format(my_power_two('a', verbose=True)))
