# hw08.py

#1
a = [1, 2, 3, 4]
a[0], a[3] = a[3], a[0]
print(a)
# [4, 2, 3, 1]

print('---------')

#2
lst = [40, 20, 30, 10]
lst[0], lst[3] = lst[3], lst[0]
print(lst)


print('---------')

#3
arr = [3, 6, 9, 12]
arr[0], arr[2] = arr[2], arr[0]
print(arr)


print('---------')

#4
a = [1, 2, 3]
b = a
print(id(a) == id(b))
# True

print('---------')

#5
x = 42
y = 42
print(id(x) == id(y))
# True

print('---------')

#6
def swap_func(arr: list):
    even_first = None
    even_first_idx = None
    odd_last = None
    odd_last_idx = None
    for i in range(len(arr)):
        if arr[i] % 2 == 0 and even_first == None:
            even_first = arr[i]
            even_first_idx = i
        if arr[i] % 2 != 0:
            odd_last = arr[i]
            odd_last_idx = i
    if even_first_idx != None and odd_last != None:
        arr[even_first_idx], arr[odd_last_idx] = arr[odd_last_idx], arr[even_first_idx]
        
a = [3, 6, 7, 4, 9, 10, 13]
print(a)
swap_func(a)
print(a)

print('---------')

#7
a = [3, 4, 5, 64, 31, 7, 12]

def find_max(arr: list)-> float:
    max = float('-inf')
    for i in range(len(arr)):
        if arr[i] > max:
            max = arr[i]
    
    return max

print('최대값:', find_max(a))

print('---------')

#9
def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        # 빈칸에 들어갈 코드
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

data = [64, 25, 12, 22, 11]
print(selection_sort(data))

print('---------')

#10
dict1 = { 'a': 10, 'b': 20, 'c': 30 }

def dict_sum(dic: dict)-> int:
    return sum(dic.values())

result = dict_sum(dict1)
print('합:', result)
    
print('---------')