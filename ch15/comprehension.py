# comprehension.py

# 1. 리스트 컴프리헨션 : 새 리스트 생성
# [표현식 for 변수 in iterable [if 조건]]
# 표현식(Expression) = 값을 만들어내는 코드

numbers = [1,2,3,4]
squared = [x**2 for x in numbers]
print(squared)

print('----------')
even_numbers = [x for x in numbers if x % 2 == 0]
print(even_numbers)

squared_plus = [x**2+1 for x in numbers if x % 2 == 0]  
# 조건식에 맞는 item 을 표현식에 대입해서 생성
print(squared_plus)

print('----------')


# 2. 딕셔너리 컴프리헨션 : 새 딕셔너리 생성
# {key표현식 : value표현식 for 변수 in iterable [if 조건]}

squared_dict = {x: x**2 for x in range(5)}
print(squared_dict)

print('----------')
even_squared_dict = {x: x**2 for x in range(10) if x %2 == 0}
print(even_squared_dict)

print('----------')
# 과목별 점수를 포함한 딕셔너리 생성
# 1. 0점으로 초기화
subjects = ['수학', '영어', '역사']
scores = {subject: 0 for subject in subjects}
print(scores)

print('----------')
# 2. 과목별 점수로 초기화
# zip() 
# : 여러개의 반복가능한 객체에서 같은 위치의 요소들을 묶어주는 함수
subjects = ['수학', '영어', '역사']
score_val = [20, 49, 98]
scores = {subject : score for subject, score in zip(subjects, score_val)}
print(scores)
print(dict(zip(subjects, score_val)))

scores = {subject : "합격" 
          for subject, score in zip(subjects, score_val) 
          if score >= 50
          }
print(scores)

# for subject, score in zip(subjects, score_val):
#     print(subject, score)

print('----------')


# 3. 제너레이터 컴프리헨션 : 새 이터레이터 생성
# (표현식 for 변수 in iterable [if 조건])

gen = (i*i for i in range(1,10))

print(type(gen))
print(gen)
for item in gen:
    print(item)