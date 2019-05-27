# 1
def swap(target_list, item_index1,  item_index2):
    target_list[item_index1], target_list[item_index2] = target_list[item_index2], target_list[item_index1]


a = [1, 2, 3, 4, 5, 6]

swap(a, 0, 1)

print(a)


# 3

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

# 4

autos = [

  {"brand": "Ford", "model": "Mustang", "year": 1964, "price": 4000},

  {"brand": "Ford", "model": "Mondeo", "year": 1999, "price": 3000},

  {"brand": "Ford", "model": "Fiesta", "year": 2003, "price": 4200},

  {"brand": "Nissan", "model": "Primera", "year": 1997, "price": 3100},

  {"brand": "BMW", "model": "X3", "year": 2001, "price": 5000},

  {"brand": "Nissan", "model": None, "year": 1964, "price": None},

  {"brand": "VW", "model": "Passat", "year": 1996, "price": 1200},

  {"brand": "BMW", "model": "X5", "year": 2010, "price": 7500},

  {"brand": "Renault", "model": "Megane", "year": 1999, "price": 2300}

]

autos_sorted_with_lambda = sorted(autos, key=lambda x: x['price'] or 0, reverse=True)

for a in autos_sorted_with_lambda:
    print(a)

print('-----------')


def my_sort_func(items):
    if items['price'] is None:
        return 0
    else:
        return items['price']


autos_sorted_with_my_func = sorted(autos, key=my_sort_func, reverse=True)

for a in autos_sorted_with_my_func:
    print(a)
