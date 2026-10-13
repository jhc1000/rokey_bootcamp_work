# rev_iterator.py

class ReverseIterator:
    def __init__(self, data):
        self.data = data
        self.position = len(data)-1
    def __iter__(self):
        return self
    def __next__(self):
        if self.position < 0:
            raise StopIteration
        result = self.data[self.position]
        self.position -= 1
        return result
    
if __name__ == "__main__":
    data = [1,2,3,4,5]
    ri = ReverseIterator(data)
    for item in ri:
        print(item)
        
    # print(next(ri))
    # print(next(ri))
    # print(next(ri))
    # print(next(ri))
    # print(next(ri))
    # print(next(ri))     # StopIteration
    
        
    print("__iter__" in dir(ri))
    print("__next__" in dir(ri))
    