def suppress(exceptions):
    def inner(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                if issubclass(type(e), exceptions):
                    print('Suppressed exception')
                else:
                    raise e
        return wrapper
    return inner


@suppress((ZeroDivisionError, TypeError))
def divide(a, b):
    if type(a) == str or type(b) == str:
        TypeError('Operands cannot be strings ')
    return a / b


print(divide(10, 5))
print(divide(10, 0))
print(divide(10, 'abc'))
