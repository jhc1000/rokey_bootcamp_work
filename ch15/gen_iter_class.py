# gen_iter_class.py

class MyIterator:
    def __init__(self):
        self.data = 1
    def __iter__(self):
        return self
    def __next__(self):
        result = self.data * self.data
        if self.data >= 10:
            raise StopIteration
        self.data += 1
        return result
    

iter_a = MyIterator()
print(iter_a)
print(next(iter_a))
for i in iter_a:
    print(i)
print(next(iter_a)) # StopIteration
    
    
# gen = (i*i for i in range(1,10))

# 간단하고 한번 흐르게 할 데이터 -> 제너레이터 컴프리헨션
# 상태/제어/객체재사용 필요 -> 이터레이터 클래스