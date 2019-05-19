s = "English = 78 Science = 83 Math = 68 History = 65"

sum_of_numbers = 0
for word in s.split():
    try:
        sum_of_numbers = sum_of_numbers + int(word)
    except ValueError:
        continue

print(str(sum_of_numbers))
