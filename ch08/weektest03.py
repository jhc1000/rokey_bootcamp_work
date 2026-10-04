# weektest03.py

#7-1
x = 10
def example1():
    x = 20
    print(x)

example1()
print(x)

print('----------')

#7-2
x = 5
def example2():
    x = 15
    print(x)

example2()
print(x)

print('----------')

#8-1
def list_max(num_list):
    max = num_list[0]
    for num in num_list:
        if num > max:
            max = num
    print(max)
    

print('----------')

#8-2
numbers = [42, 17, 23, 56, 9, 34]

def list_min(num_list: list)-> int:
    min = num_list[0]
    for num in num_list:
        if num < min:
            min = num
    return min

result = list_min(numbers)
print('최솟값:', result)

print('----------')