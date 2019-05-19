s = "spam and eggs or eggs with spam"

# method 1
count = {}
for char in s:
    if char in count.keys():
        count[char] = count[char] + 1
    else:
        count[char] = 1

print(count)

# method 2
count_2 = {}
unique_s = "".join(set(s))
for char in unique_s:
    count_2[char] = s.count(char)

print(count_2)
