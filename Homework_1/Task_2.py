a = {'a': 1, 'b': 4, 't': 67}
b = {'c': 4, 'e': 1, 'a': 4, 't': 7, 'y': 11}

# 2.1
common_keys = []
for key in a.keys():
    if key in b.keys():
        common_keys.append(key)

print("Common keys: " + str(common_keys))

# 2.2
only_b_keys = []
for key in b.keys():
    if key not in a.keys():
        only_b_keys.append(key)

print("Keys present only in b: " + str(only_b_keys))

# 2.3
ab = a
for key in b.keys():
    if key in ab.keys():
        ab[key] = ab[key] + b[key]
    else:
        ab[key] = b[key]

print("Combined dict: " + str(ab))
