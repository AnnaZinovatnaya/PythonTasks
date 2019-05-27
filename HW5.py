import time


def timer(func):
    def wrapper(number):
        start_time = time.time()
        res = func(number)
        print('Time = ' + str(time.time() - start_time))
        return res

    return wrapper


def counted(func):
    counter = 0

    def wrapper(number):
        nonlocal counter
        counter += 1
        print('Call ' + str(counter))

        return func(number)

    return wrapper


def cached(func):
    history = {}

    def wrapper(number):
        if number in history.keys():
            print("Return from history")
        else:
            print("Calculate")
            history[number] = func(number)
        return history[number]

    return wrapper


def once(func):
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
    return number ** 3


print(my_power_three(3))
print(my_power_three(4))


@timer
@counted
@cached
def my_power_two(number):
    return number ** 2


print(my_power_two(1))
print(my_power_two(4))
print(my_power_two(6))
print(my_power_two(1))

