class MyRange:
    def __init__(self, start, stop=None, step=None):
        if stop is None and step is None:
            stop = start
            self.start = 0
            self.stop = stop
            self.step = 1
        elif step is None:
            self.start = start
            self.stop = stop
            self.step = 1
        else:
            self.start = start
            self.stop = stop
            self.step = step
        
        self.current = self.start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.stop:
            raise StopIteration
        self.current += self.step
        return self.current - self.step


for el in MyRange(10):
    print(el)
for el in MyRange(5, 10):
    print(el)
for el in MyRange(2, 21, 2):
    print(el)
    