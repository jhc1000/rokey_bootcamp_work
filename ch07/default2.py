# default2.py

# # 기본 매개변수 없이 사용
# def person_c(height, weight, age):
#     print("체중:", height, "몸무게:", weight, "나이:", age)

# person_c(168, 55, 23)

print('----------')

# 일부 기본 매개변수 사용 : 뒤에서부터 채운다
def person_c(height, weight=50, age=22):
    print("체중:", height, "몸무게:", weight, "나이:", age)
    
# def person_c(height, weight=50, age): # SyntaxError 기본 매개변수는 순서때문에 마지막에 있어야 한다.
#     print("체중:", height, "몸무게:", weight, "나이:", age)

# 인수는 앞쪽부터 설정
person_c(168, 55, 23)
person_c(168, 55)
person_c(168)

print('----------')

# 1. 모든 매개변수에 기본값 설정가능
# 2. 기본값이 있더라도 인수 설정 가능(인수 우선처리)
# 3. 부분 매개변수에 기본값 설정시, 뒤에서부터 설정할 것
# 4. 인수 전달시 앞에서부터 설정할 것.

# 위치 인수 : 순서대로 전달하는 함수
person_c(168, 55, 23)

# 키워드 인수 : (매개변수) 이름을 지정해서 전달하는 인수
person_c(weight=55, height=139, age=87)

person_c(178, age=87)

# 활용 예시
print("hi", "hello", end=" ", sep="/")