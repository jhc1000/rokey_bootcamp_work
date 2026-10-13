# iterator2.py

class MyIterator:
    def __init__(self, data):
        self.data = data
        self.position = 0
    def __iter__(self):   # __iter__() 스폐셜 메서드에 iterator 변환 내장되어있음
        return self
    def __next__(self):   # __next__() 메서드는 구현해야함
        if self.position >= len(self.data):
            raise StopIteration
        result = self.data[self.position]
        self.position += 1
        return result

if __name__ == "__main__":
    data = [1,2,3]
    i = MyIterator(data)
    print(type(i))      # <class '__main__.Myiterator'>
    for item in i:
        print(item)
        
    # for item in i:
    #     print(item)
        
    # print(next(i))    # 1
    # print(next(i))    # 2
    # print(next(i))    # 3
    # print(next(i))    # StopIteration
    
    # print(MyIterator.__next__(i)) # 1
    
    print('-----------')

    # print(dir(i))
    # print(dir(data))
    
    print("__iter__" in dir(data))
    print("__next__" in dir(data))
    
    print("__iter__" in dir(i))
    print("__next__" in dir(i))