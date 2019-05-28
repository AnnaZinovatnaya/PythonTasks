def check(password):
    if len(password) < 4:
        return False

    allowed_symbols = [chr(x) for x in range(97, 123)]
    allowed_symbols.extend([chr(x) for x in range(48, 58)])

    digit_count = 0
    char_count = 0

    for ch in password:
        if ch.isalpha() and ch.isupper():
            return False
        if ch.isdigit():
            digit_count += 1
        if ch.isalpha():
            char_count += 1

    if char_count % 2 == 0 or digit_count % 2 == 1:
        return False

    return True


print(check('45'))              # False
print(check('ghghjhghgeGG33'))  # False
print(check('fghghjhghge336'))  # False
print(check('fghghjhghg33'))    # False
print(check('ffghghjhghg33'))   # True

