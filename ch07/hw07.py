# hw07.py

#3
def calculate_area(length, width=10):
    return length * width
print(calculate_area(5)) # 50
print(calculate_area(5, 20)) # 100

print('-----------')

#4
# def add_numbers(a, b):
#     return a + b
# print(add_numbers(10))

def add_numbers(a, b=5):
    return a + b
print(add_numbers(10))

def add_numbers(a, b):
    return a + b
print(add_numbers(10, 5))

print('-----------')

#5
def inner_function(x, y):
        return x + y
def outer_function(x, y):
    return inner_function(x, y)

add_10 = outer_function(10, 5)
print(add_10)

print('----------')

#6 

# def add_numbers(a, b):
#     result = a + b
# print(result)

def add_numbers(a, b):
    result = a + b
result = 0
print(result)

def add_numbers(a, b):
    result = a + b
    return result
result = add_numbers(10, 55)
print(result)

print('----------')


#7
def message() :
    print("A")
    print("B")
message()
print("C")
message()

# A
# B
# C
# A
# B

print('----------')

#8
print("A")
def message() :
    print("B")
print("C")
message()

# A
# C
# B

print('----------')

#9
def check_odd_even(num: int) -> str:
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"
    
print(check_odd_even(4))  
print(check_odd_even(7))   

print('----------')

#10
def calculate_average(num_list: list) -> float:
    sum = 0
    for i in num_list:
        sum += i
    return sum / len(num_list)

num_list = [10, 20, 30, 40, 50]
average = calculate_average(num_list)
print("평균: ", average)

print('----------')


    