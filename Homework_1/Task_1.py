data = [1, 4, 6, 7, 2, 1, 7, 8, 9, 5, 7, 3, 6, 2, 7, 43, 54, 13]

# 1.1
print("1.1")
print("Max value: " + str(max(data)))
print("Min value: " + str(min(data)))
print("Index of max value: " + str(data.index(max(data))))
print("Index of min value: " + str(data.index(min(data))))

# 1.2
print("1.2")
unique_data = list(set(data))
value_count = [data.count(x) for x in unique_data]

index_of_common_value = value_count.index(max(value_count))
print("First most common value: " + str(unique_data[index_of_common_value]))
value_count[index_of_common_value] = 0

index_of_common_value = value_count.index(max(value_count))
print("Second most common value: " + str(unique_data[index_of_common_value]))
value_count[index_of_common_value] = 0

index_of_common_value = value_count.index(max(value_count))
print("Third most common value: " + str(unique_data[index_of_common_value]))

# 1.3.1
print("1.3.1")
res = list(set(data))
print("List with unique values (different order): " + str(res))

# 1.3.2
print("1.3.2")
res = []
for element in data:
    if element not in res:
        res.append(element)

print("List with unique values (same order): " + str(res))
