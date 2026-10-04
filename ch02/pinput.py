# pinput.py
# 주석 ctrl + /
# print("첫 번째 정수를 입력:")
# ra=input()
# rb=input("두 번째 정수를 입력:")
# rc=ra+rb
# print(type(ra))
# print(type(rb))
# print(type(rc))
# print(ra, "+", rb, "값은", rc, "이다")

# 숫자 + 숫자 = 던셈결과
# 문자열 + 문자열 = 연결된 문자열

print('--------')

# 문제 => 덧셈을 하고 싶으나 자료형이 맞지 않음
# 해결방법 => 문자열 -> 정수형 변환 : int()

# int(데이터) : 정수형
# float(데이터) : 실수형
# str(데이터) : 문자열

print("첫 번째 정수를 입력:")
ra=input()
rb=input("두 번째 정수를 입력:")
print(type(ra))
print(type(rb))
ra = int(ra)
rb = int(rb)
rc=ra+rb
print(type(rc))
print(ra, "+", rb, "값은", rc, "이다")
