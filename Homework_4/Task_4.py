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


def my_sort_func(item):
    if item['price'] is None:
        return 0
    else:
        return item['price']


autos_sorted_with_my_func = sorted(autos, key=my_sort_func, reverse=True)

for a in autos_sorted_with_my_func:
    print(a)

