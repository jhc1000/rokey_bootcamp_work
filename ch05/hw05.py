# hw05.py

#1 
과일 = ["사과", "귤", "수박"]
for 변수 in 과일:
    print(변수)
    
print('---------')

#2
변수 = [10, 20, 30]
for i in 변수:
    print(i)
    
print('---------')

#3
가격리스트 = [100, 200, 300]
for price in 가격리스트:
    price += 10
    print(price)
    
print('---------')

#4
리스트 = ['dog', 'cat', 'parrot']

for name in 리스트:
    len = 0
    for i in name:
        len += 1
    print(name, len)
    
print('---------')

#5
리스트 = ["가", "나", "다", "라"]
for name in 리스트:
    if name == '가':
        continue
    print(name)

print('---------')

#6
리스트 = [3, -20, -3, 44]
for n in 리스트:
    if n < 0:
        print(n)

print('---------')

#7
for year in range(2002, 2051):
    if (year - 2002) % 4 == 0:
        print(year)
        
print('---------')

#9
sum = 0
n = 1
while n <= 100:
    sum += n
    n += 1
print(sum) 

print('---------')

#10
for i in range(1,31):
    if i % 2 == 0:
        print(i, "짝수")
    else:
        print(i, "홀수")
        
print('---------')


#11
list_1 = []
list_2 = []
for i in range(1,31):
    if i % 2 == 0:
        list_2.append(i)
    else:
        list_1.append(i)

print("홀수 리스트", list_1)
print("짝수 리스트", list_2)

print('---------')