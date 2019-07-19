class BackwardsIterator:
    def __init__(self, data):
        self.data = data
        self.current = len(data) - 1
    def __iter__(self):
        return self
    def __next__(self):
        if self.current < 0:
            raise StopIteration
        self.current -= 1
        return self.data[self.current + 1]


for el in BackwardsIterator([1, 2, 3, 4, 5, 6, 7, 8, 9]):
    print(el)
