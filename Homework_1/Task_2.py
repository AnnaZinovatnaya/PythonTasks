from collections import Counter

a = {'a': 1, 'b': 4, 't': 67}
b = {'c': 4, 'e': 1, 'a': 4, 't': 7, 'y': 11}

# 2.1
# solution without Counter
common_keys = []
for key in a.keys():
    if key in b.keys():
        common_keys.append(key)

print('Common keys: ' + str(common_keys))

# solution with Counter
inter = Counter(a) & Counter(b)
print('Counter solution: ' + str(list(set(inter.elements()))))


# 2.2
# solution without Counter
only_b_keys = []
for key in b.keys():
    if key not in a.keys():
        only_b_keys.append(key)

print('Keys present only in b: ' + str(only_b_keys))

# solution with Counter
print('Counter solution: ' + str(list(Counter(b).keys() - Counter(a).keys())))


# 2.3
# solution without Counter
ab = a
for key in b.keys():
    if key in ab.keys():
        ab[key] = ab[key] + b[key]
    else:
        ab[key] = b[key]

print('Combined dict: ' + str(ab))

# solution with Counter
summ = Counter(a) | Counter(b)
print('Counter solution: ' + str(dict(summ)))
