class MyIZip:
    def __init__(self, *args):
        self.data = []
        for arg in args:
            self.data.append(arg)
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        for collection in self.data:
            if self.current == len(collection):
                raise StopIteration

        self.current += 1
        
        result = ()
        for collection in self.data:
            result = result + (collection[self.current - 1],)
        return result


for ziped_value in MyIZip(['a', 'b', 'c', 'd'], [1, 2, 3, 4, 5]):
    print(ziped_value)

for ziped_value in MyIZip(['a', 'b', 'c', 'd'], [1, 2, 3, 4, 5], [10, 20, 30]):
    print(ziped_value)

for ziped_value in MyIZip(['a', 'b', 'c', 'd']):
    print(ziped_value)
