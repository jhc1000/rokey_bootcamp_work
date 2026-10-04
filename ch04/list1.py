# list1.py

candy0 = '딸기맛'
print(candy0)
candy1 = '레몬맛'
print(candy1)
candy2 = '수박맛'
print(candy2)
candy3 = '박하맛'
print(candy3)
candy4 = '우유맛'
print(candy4)

candies = ['딸기맛', '레몬맛', '수박맛', '박하맛', '우유맛']
print(candies)
print(type(candies))

# 리스트변수명[접근할인덱스]
print(candies[1])
print(candies[2])

print(type(candies[1]))
print(type(candies[2]))

print('--------')
a = 10
lista = ['list', 1, 0.7, True, [2,3], a<3]
print(lista)
print(type(lista))

print(lista[3])
print(type(lista[3]))
print(lista[4][0])
print(lista[4][1])
print(type(lista[4][1]))


print('--------')
ca = [10, 11, 21]
print(ca)
print(ca[0], end=" ")
print(ca[1], end=" ")
print(ca[2], end=" ")

print('--------')

a = [1, 2, 3, 4, 5]

a[2] = 30
print(a)

a[3] = 40
print(a)

a[0] = 'hi'
a[1] = False
print(a)