nested_list = [
	['a', 'b', 'c'],
	['d', 'e', 'f', 'h', False],
	[1, 2, None],

]

class FlatIterator:

    def __init__(self, some_list):
        self.some_list = some_list

    def __iter__(self):
        self.cursor = 0
        self.cursor2 = -1
        return self

    def __next__(self):
        self.cursor2 +=1
        if self.cursor2 > len(self.some_list[self.cursor])-1:
            self.cursor +=1
            self.cursor2 = 0
            if self.cursor > len(self.some_list)-1:
                raise StopIteration
        return self.some_list[self.cursor][self.cursor2]

for i in FlatIterator(nested_list):
    print(i)

flat_list = [item for item in FlatIterator(nested_list)]
print(flat_list)

def flatgenerator(some_list):
    cursor = 0
    cursor2 = -1
    while True:
        cursor2 +=1
        if cursor2 > len(some_list[cursor])-1:
            cursor +=1
            cursor2 = 0
            if cursor > len(some_list)-1:
                raise StopIteration
        yield some_list[cursor][cursor2]

for item in flatgenerator(nested_list):
    print(item)
        
