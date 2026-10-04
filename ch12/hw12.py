# hw12.py

# with open("test.txt", "w") as file:
#     file.write("Hello, World!")
# print(file.closed)

print('--------')

#6

# path="./pizza_file1.txt"
# mode="w"
# pizza_list = ["페퍼로니피자",
#               "치즈피자",
#               "콤비네이션피자"]
# with open(path, mode, encoding='utf-8') as file:
#     for item in pizza_list:
#         data = "%s\n" % item
#         file.write(data)

print('--------')

#7

# path="./pizza_file1.txt"
# mode="w"
# pizza_list = ["페퍼로니피자",
#               "치즈피자",
#               "콤비네이션피자"]
# price_list = [3000, 3200, 3500]
# with open(path, mode, encoding='utf-8') as file:
#     for i in range(len(pizza_list)):
#         data = "%s %d\n" % (pizza_list[i], price_list[i])
#         file.write(data)
        
print('--------')

#8

# path="./pizza_file1.txt"
# mode="a"
# pizza_list = ["불고기피자",
#               "해산물피자"]
# price_list = [3600, 3800]
# with open(path, mode, encoding='utf-8') as file:
#     for i in range(len(pizza_list)):
#         data = "%s %d\n" % (pizza_list[i], price_list[i])
#         file.write(data)

print('--------')

#9
# path="./pizza_file1.txt"
# mode="r"
# with open(path, mode, encoding='utf-8') as file:
#     lines = file.readlines()
#     for line in lines:
#         print(line, end="")
        
print('--------')


#10
path="./pizza_file1.txt"
mode="r"
pizza_list = []
with open(path, mode, encoding='utf-8') as file:
    lines = file.readlines()
    for line in lines:
        pizza_item = line.split()
        pizza_list.append(pizza_item[0])
        
print(pizza_list)
