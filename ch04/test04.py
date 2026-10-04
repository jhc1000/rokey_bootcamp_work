# test04.py

#1
nums = [1,2,3]
print(nums)

print('----------')

#2
fruits = []
print(fruits) # []
fruits.append('자몽')
print(fruits) # ['자몽']
fruits.append('멜론')
print(fruits) # ['자몽', '멜론']
fruits.append('레몬')
print(fruits) # ['자몽', '멜론', '레몬']

print('----------')

#3
fruits = ['자몽', '멜론', '레몬']
print(fruits[1]) # 멜론

print('----------')

#4
fruits = ['자몽', '멜론', '레몬']
print(fruits)
fruits.remove('자몽')
print(fruits)

print('----------')

#5
nums = (1,2,3)
print(nums)

print('----------')

#6
my_tuple = (3.14, 2.71)
print(my_tuple) # (3.14, 2.71)
print(my_tuple[1]) # 2.71

#7 
my_var = 1,
print(type(my_var)) # tuple

my_var = (1,)
print(type(my_var)) # tuple

my_var = (1)
print(type(my_var)) # int

my_var = 1, 2
print(type(my_var)) # tuple

print('----------')

#8
alice = {'성별': '여', '나이': 13, '혈액형': 'AB'}
alice['나이'] = 14
print(alice['나이'])

print('----------')
