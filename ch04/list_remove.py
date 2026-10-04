# list_remove.py

 # 값 제거하기
 # 리스트명.remove(제거할_값)
 
subject = ['국어', '수학', '영어', '국사']
subject.append('영어')
print(subject)
print(subject[2])
print(subject[3])

print('--------')

subject.remove('영어')
print(subject)
print(subject[2])
print(subject[3]) # IndexError

print('--------')

clovers = ['클로버1', '클로버2', '클로버3']
print(clovers[1])

del clovers[1]
print(clovers)

print(clovers[1])