# recursive.py

# 재귀함수
# def 함수명(매개변수):
#     코드블록
#     함수명(인수)
#     return 반환값

def count_down(n):
    if n == 0: # 기저 조건
        print("완료!")
        return
    print(n)
    count_down(n-1) # 재귀 단계 

count_down(10)

print('-----------')

def factorial(num):
    if num == 1:
        return 1
    return num * factorial(num-1)

print(factorial(5))
print(factorial(10))

print('-----------')

# 실무 활용 예시
# 폴더 탐색, 알고리즘(트리구조)

