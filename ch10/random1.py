# ramdom1.py

import random

animals = ['체셔고양이', '오리', '도도새', '호랑이', '고래']
print(random.choice(animals))
print(random.choice(animals))
print(random.choice(animals))

print('-----------')
warriors = ['유비', '관우', '장비', '조운', '조조', '제갈량']

print(random.sample(warriors, 2))
print(random.sample(warriors, 2))
print(random.sample(warriors, 2))

print('-----------')
print("행운의 숫자:")
print(random.randint(1,100))
print(random.randint(1,100))
print(random.randint(1,100))
print(random.randint(1,100))
print(random.randint(1,100))
print(random.randint(1,100))

print('-----------')
numbers = range(1,101)
print(random.sample(numbers, 6))