# hw04.py

#1 
movie_rank = ['하얼빈', '무파사:라이온킹', '소방관']
print(movie_rank)

print('--------')

#2
movie_rank.append('위키드')
print(movie_rank)

print('--------')

#3
movie_rank = ['하얼빈', '무파사:라이온킹', '소방관', '위키드']
movie_rank.insert(3, '모아나2')
print(movie_rank)

print('--------')

#4 
del movie_rank[2]
print(movie_rank)

print('--------')

#5
nums = [1, 2, 3, 4, 5]
sum1 = 0
for i in nums:
    sum1 += i
print(sum1) 

print('--------')

#6
cook = ["피자", "김밥", "만두", "양념치킨", "족발", "피자", "김치만두", "쫄면", "쏘세지", "라면", "팥빙수", "김치전"]
print(len(cook))

print('-------')

#8
t = ('a', 'b', 'c')
t_list = list(t)
t_list[0] = 'A'
t = tuple(t_list)
print(t)

print('-------')

#9
dict1 = {'메로나':1000, '폴라포':1200, '빵빠레':1800}

#10
dict1['죠스바'] = 1200
dict1['월드콘'] = 1500
print(dict1)

print('-------')

#11
dict1['메로나'] = 1300
print(dict1)

print('-------')
