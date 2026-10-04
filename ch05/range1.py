# range1.py

# range(인수) # 0 ~ 인수-1 
# range(인수1, 인수2) # 시작정수 끝정수-1
# range(인수1, 인수2, 인수3) # 시작정수 끝정수-1 증감정수(step) 


print(range(10)) # range(0, 10)
print(type(range(10)))
print(list(range(10))) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(list(range(0, -10, -1)))
print(list(range(-10, -1)))

print(list(range(8, 14, 2)))

# for 변수 in range(인수):
#     코드블록

for i in range(3):
    print(i)