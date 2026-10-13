# iterator1.py

# 이터레이터 생성 방법
# 1. iter() 함수 사용
data = [1,2,3]
iterator = iter(data)  
print(iterator)

# dir() : 객체의 속성을 보여주는 함수
# hasattr() : 객체에 주어진 이름의 속성이 있는지 여부를 반환

# __iter__() 메서드의 포함 여부 확인
print("__iter__" in dir(data))  # True     # 리스트 안에 __iter__() 있는지
print("__next__" in dir(data))  # False    # 리스트 안에 __next__() 있는지

print(hasattr(data, "__iter__"))    # True
print(hasattr(data, "__next__"))    # False

print('-------------')
print("__iter__" in dir(iterator))  # True  
print("__next__" in dir(iterator))  # True