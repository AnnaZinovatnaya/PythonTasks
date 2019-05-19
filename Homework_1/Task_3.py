print("Input a number:")

try:
    number = int(input())
except ValueError:
    print("This is not a number")
    exit(0)

if number < 0:
    print("This is not a positive number")
    exit(0)


def generate_prime_numbers(num):
    prime_numbers = []
    for x in range(2, num + 1):
        for y in range(2, x):
            if x % y == 0:
                break
        else:
            prime_numbers.append(x)
    return prime_numbers


if number == 1:
    number_count = {1: 1}
else:
    number_count = {}

while number != 1:
    for x in generate_prime_numbers(number):
        if number % x == 0:
            if x in number_count.keys():
                number_count[x] = number_count[x] + 1
            else:
                number_count[x] = 1

            number = int(number / x)

res = ""
for key in number_count:
    if number_count[key] == 1:
        res = res + str(key) + " * "
    else:
        res = res + str(key) + "^" + str(number_count[key]) + " * "
print(res[0:-3])
