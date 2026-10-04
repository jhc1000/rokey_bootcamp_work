# map_func.py

# map(함수, 이터레이터)
# 1. 기능/동작: 이터레이터에 함수 적용
# 2. 매개변수: 적용함수, 이터레이터
# 3. 반환값: map객체 (이터레이터)


def square(x):
    return x ** 2

numbers=[1,2,3,4,5]
squared_numbers=map(square, numbers)
print(list(squared_numbers))

numbers=[1,2,3,4,5]
squared_numbers=map(lambda x:x**2, numbers)
print(list(squared_numbers))    # list(range(4)) 같이 list() 변환을 거쳐야함
# print(type(squared_numbers))   
# print(squared_numbers)
for i in squared_numbers:       # 이터레이터는 1번만 꺼내쓸수있다
    print(i)

# 람다 함수 장점
# 1. 짧은 함수 간결하게 표현
# 2. 함수를 값처럼 바로 전달 가능
# 3. 일회성 함수를 만들때 편리함
# 4. 다른 함수와 결함 적합