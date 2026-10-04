# weektest2.py

#1
a = 3.14     
b = True
c = "False"

print(type(a))
print(type(b))
print(type(c))

print('--------')

# num1 = int(input('1번째 숫자를 입력하세요(ex:6):'))
# num2 = int(input('2번째 숫자를 입력하세요(ex:2):'))

# add = num1 + num2
# sub = num1 - num2
# mul = num1 * num2
# div = num1 / num2

# print(f"{num1} + {num2} = {add}")
# print(f"{num1} - {num2} = {sub}")
# print(f"{num1} * {num2} = {mul}")
# print(f"{num1} / {num2} = {div}")

print('-------------')

# score = int(input('점수를 입력하시오'))
# if score >= 90:
#     print("A학점")
# elif score >= 80:
#     print("B학점")
# elif score >= 70:
#     print("C학점")
# else:
#     print("F학점")
    
print('-------------')

fruits = ["banana", "peach", "lemon", "grape"]
print(fruits[2])


print('-------------')

student3 = {"나이": 22, "직업": "학생", "취미": "게임"}
student3["도시"] = "수원"
print(student3.keys())

print('-------------')

Numbers = [1, 2, 3, 4, 5]
for i in Numbers:
    print(i, end=" ")
print()


print('-------------')

fruits = ['바나나', '파인애플', '복숭아', '사과', '포도']
for i in fruits:
    print(i)
    if i == '사과':
        print("사과를 찾았습니다!")



print('-------------')

def solution(a, b):
		sum = a + b
		sub = a - b
		multi = a * b
		return sum, sub, multi

num1 = float(input('1번째 수를 입력하세요(ex:6.2):'))
num2 = float(input('2번째 수를 입력하세요(ex:212):'))

result = solution(num1, num2)
print(f"{num1}, {num2}의 합은 {result[0]}")
print(f"{num1}, {num2}의 차는 {result[1]}")
print(f"{num1}, {num2}의 곱은 {result[2]}")


print('-------------')

n = 10
def sum_1_to_n(n):
    total = 0
    for i in range(1, n+1):
        total += i
    return total

print(sum_1_to_n(n))

print('-------------')
	
