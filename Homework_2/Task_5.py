import random


def generate_password(password_len):
    chars = []
    for digit in range(48, 58):
        chars.append(chr(digit))
    for capital_letter in range(65, 91):
        chars.append(chr(capital_letter))
    for letter in range(97, 123):
        chars.append(chr(letter))
        
    password = ""
    for i in range(0, password_len):
        password += chars[random.randint(0, (len(chars) - 1))]
        
    return password
    
    
user_input = None

while user_input != 0:
    print("Input password length (or 0 to exit):")
    user_input = input()
    try:
        user_input = int(user_input)
    except ValueError:
        print("This is not a number")
        continue

    if user_input < 0:
        print("This is not a positive number")
        continue
        
    if user_input == 0:
        continue
    else:
        print(generate_password(user_input))
