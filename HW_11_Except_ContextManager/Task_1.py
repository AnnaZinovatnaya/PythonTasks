def suppress(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f'Suppressed exception: {e}')
    return wrapper


@suppress
def divide(a, b):
    return a / b


divide(10, 0)
