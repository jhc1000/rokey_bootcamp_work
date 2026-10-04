# test05.py

#1 
for num in [3, 1, 2]:
    print(num)
# 3
# 1
# 2 
print('---------')

#2 
for num in range(2):
    print(num)
# 0
# 1
print('---------')

#3
clovers = ['클로버1', '클로버2', '클로버3']
for clover in clovers:
    print(clover)

clovers = ['클로버1', '클로버2', '클로버3']
count = 0 
while count < 3:
    print(clovers[count])
    count = count +1
    
print('---------')

#4 
clovers = ['클로버1', '클로버2', '클로버3']
for i in range(len(clovers)):
    print(clovers[i])
    
print('---------')

#5
count = 0 
while count < 3:
    print(count)
    count = count +1
# 0
# 1
# 2
print('---------')

#6
count = 1
while count < 4:
    count = count + 1
    print(count)
    
print('---------')

#7
# 범위(0~5)내 홀수를 출력하는 코드
count = 0 
while count <=5:
    if count % 2 != 0:
        print(count)
    count = count + 1
    
# 1
# 3 
# 5

print('---------')

# #8
# price = 0
# while price != -1:
#     price = int(input('가격을 입력하세요 (종료:-1): '))
#     if price > 10000:
#         print('너무 비싸요.')
#     elif price > 5000:
#         print('괜찮은 가격이네요.')
#     elif price > 0:
#         print('정말 싸요.')
        
# print('---------')

#9 
num = 0
while num <= 100:
    if num % 3 == 0:
        print(num, end=" ")
    num += 1
print()

for num in range(0, 101):
    if num % 3 == 0:
        print(num, end=" ")
print()     
print('--------')

#10 
num = 0
while num < 10:
    num += 1
    if num % 3 == 0:
        continue
    print(num, end=" ")
print()

for num in range(10):
    if (num+1) % 3 == 0:
        continue
    print(num+1, end=" ")
print()

print('--------')

#11
# for
# num = int(input('총합을 구하려는 수를 입력하세요.'))
# sum = 0
# for i in range(1, num+1):
#     sum += i
# print("1 부터", num, "까지의 총합은", sum, "이다.")

# while
# num = int(input('총합을 구하려는 수를 입력하세요.'))
# sum = 0
# i = 0
# while i < num:
#     i = i + 1 
#     sum += i
# print("1 부터", num, "까지의 총합은", sum, "이다.")

# while break
# num = int(input('총합을 구하려는 수를 입력하세요.'))
# sum = 0
# i = 0
# while True:
#     if i >= num:
#         break
#     i = i + 1 
#     sum += i
# print("1 부터", num, "까지의 총합은", sum, "이다.")

# print('--------')

#29
# for
# num1 = int(input('총합을 구하려는 첫번째 수를 입력하세요.'))
# num2 = int(input('총합을 구하려는 두번째 수를 입력하세요.'))
# sum = 0
# for i in range(num1, num2+1):
#     sum += i
# print(num1, "부터", num2, "까지의 총합은", sum, "이다.")

# while
# num1 = int(input('총합을 구하려는 첫번째 수를 입력하세요.'))
# num2 = int(input('총합을 구하려는 두번째 수를 입력하세요.'))
# sum = 0
# i = num1
# while i <= num2:
#     sum += i
#     i = i + 1 
# print(num1, "부터", num2, "까지의 총합은", sum, "이다.")

# 30
# for
# num1 = int(input('총합을 구하려는 첫번째 수를 입력하세요.'))
# num2 = int(input('총합을 구하려는 두번째 수를 입력하세요.'))
# sum = 0
# for i in range(num1, num2+1):
#     if i % 3 == 0:
#         sum += i
# print(num1, "부터", num2, "까지의 3의 배수 총합은", sum, "이다.")

# while
# num1 = int(input('총합을 구하려는 첫번째 수를 입력하세요.'))
# num2 = int(input('총합을 구하려는 두번째 수를 입력하세요.'))
# sum = 0
# i = num1
# while i <= num2:
#     if i % 3 == 0:
#         sum += i
#     i = i + 1 
# print(num1, "부터", num2, "까지의 총합은", sum, "이다.")

# #12
# for sb in range(1, 11, 1):
#     total=0
#     total=total+sb
# print(total)
# # 10

# total = 0
# for sb in range(1, 11, 1):
#     total=total+sb
# print(total, end="  ")
# print("끝")
# # 55  끝

# total = 0
# for sb in range(1, 11, 1):
#     total=total+sb
# print(total)
# # 55

# total = 0
# for sb in range(1, 11, 1):
#     total=total+1
# print(total)
# # 10

# for sb in range(1, 11, 1):
#     total = 0
#     total=total+1
# print(total)
# # 1

# print('--------')

#31
# MyName = ''
# while True:
#     MyName = input('이름을 입력하세요')
#     if MyName == 'hongkildong':
#         break
# print('확인되었습니다.')

#32
# MyName = ''
# while True:
#     MyName = input('이름을 입력하세요')
#     if MyName != 'hongkildong':
#         continue
#     else:
#         MyPass = input('패스워드를 입력하세요')
#         if MyPass == 'hahaha':
#             break
# print('확인되었습니다.')

# # 33
n = 1
for i in range(1,10):
    x = i
    b = n * x
    print(f"{n} * {x} = {b}")

print('--------')

n = 2
for i in range(1,10):
    x = i
    b = n * x
    print(f"{n} * {x} = {b}")
    
print('--------')

#36
for j in range(1,6):
    for i in range(1,10):
        print(f"{j} * {i} = {j * i}")
    print('===========')
        

print('--------')

#37
for i in range(1,6):
    for j in range(1, i+1):
        print(j, end=" ")
    print()
    
print('--------')
    
a = ['A', 'B', 'C', 'D', 'E']
for i in range(1, 6):
    for j in range(i):
        print(a[j], end=" ")
    print()
