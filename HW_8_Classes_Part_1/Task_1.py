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
