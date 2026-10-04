# for1.py

# for 변수 in 리스트:
#     코드블록

# for 변수 in 문자열:
#     코드블록

nums = [0,1,2]
for num in nums:
    print('hi')
print('for문 종료')

print('----------')

characters = ['앨리스', '도도새', '3월토끼']
for character in characters:
    print(character)
    
print('----------')

for letter in '체셔고양이':
    print(letter)

print('----------')

nums = [0,1,2]
for num in nums:
    print(num)
    print(nums)

print('----------')

hong = {"이름":"홍길동", "나이":500, "국적":"조선"}
for i in hong: # key 값을 가져온다.
    print(i)
    
print('----------')

for i in hong.items(): # item 값을 가져온다.
    print(i, type(i))
for i in hong.keys(): # key 값을 가져온다.
    print(i, type(i))
for i in hong.values(): # value 값을 가져온다.
    print(i, type(i))
print(hong)

print('----------')
