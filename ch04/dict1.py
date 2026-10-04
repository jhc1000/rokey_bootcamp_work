# dict1.py

# 딕셔너리
# 리스트 = [item1, item2, item3, ...]
# 딕셔너리 = {key1:val1, key2:val2, key3:val3, ... }

my_dict1 = {}
print(my_dict1, type(my_dict1))

my_dict2 = {0: 1, 1: -2, 2: 3.14}
print(my_dict2)

my_dict2[1] = 'k'
print(my_dict2[1])
print(my_dict2)

my_dict3 = {'이름': '앨리스', '나이': 10, '시력': [1.0, 1.2]}
print(my_dict3)

print('------------')
# 키-값 추가하기
# 딕셔너리[키] = 데이터값
my_dict3['성별'] = '여성'
print(my_dict3)

my_dict3['직업'] = '개발자'
print(my_dict3)

print('------------')
# 값 접근하기
# 딕셔너리[키]
print(my_dict3['이름'])
print(my_dict3['직업'])

print('------------')
# 각자의 데이터를 활용해서 딕셔러니를 생성하고, 추가하고, 값에 접근해보기
my_data = {'이름': '주형찬', '나이': 28, '성별': '남자', '메일':None}
print(my_data)

my_data['키'] =  173
print(my_data)

print(my_data['이름']) # 키 없으면 KeyError
print(my_data.get('주소', '없음'))
print(my_data.get('주소'))
print(my_data.get('메일'))

my_item = my_data.items()
print(my_item, type(my_item))
print(my_data.keys())
print(my_data.values())

# _MISSING = object() 

# value = my_data.get('주소', _MISSING)
# if value is _MISSING: #키 없음
# elif value is None: #키는 있고 값이 None
# else: #키도 있고 값이 있음.