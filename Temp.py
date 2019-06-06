class Person:
    def __init__(self, name, job, salary):
        self.name = name
        self.salary = salary
        self.job = job

    def __str__(self):
        return 'My name is {}. I am a(n) {} and I earn {}.'.format(self.name, self.job, self.salary)


class Manager(Person):
    def __init__(self, name, job, salary, percentage):
        self.percentage = percentage
        super().__init__(name, job, salary)


p = Person('Mary', 'sales manager', 12000)
print(p)

m = Manager('Peter', 'manager', 20000, 15)
print(m)


s = input()
allowed_chars = ['[', ']', '{', '}', '(', ')', '<', '>']

res = True
for ch in s:
    if ch not in allowed_chars:
        res = False
        print('not allowed')
        break


def is_start(char):
    if char == '[' or '{' or '(' or '<':
        return True
    return False


def is_closing_pair(char1, char2):
    if char1 == '[' and char2 == ']':
        return True
    if char1 == '{' and char2 == '}':
        return True
    if char1 == '(' and char2 == ')':
        return True
    if char1 == '<' and char2 == '>':
        return True
    return False


l = []
if res:
    for ch in s:
        if not l and is_start(ch):
            l.append(ch)
            print(l)
            continue
        if is_closing_pair(l[-1], ch):
            l.pop(-1)
            print(l)
            continue
        if is_start(ch):
            l.append(ch)
            print(l)
            continue

        res = False
        break


print(res)
