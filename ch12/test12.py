# test12.py

path = "ch12/계좌1.txt"
mode = 'w'

name_list = ["김삿갓","이수근","박혁거세"]
account_list = ["597-89-000089",
                "343-64-000064",
                "136-97-000097"] 

with open(path, mode, encoding='utf-8') as file:
    for i in range(len(name_list)):
        data = name_list[i] + " " + account_list[i] + "\n"
        file.write(data)
        
# file = open(path, mode, encoding='utf-8')
# file.write("김삿갓 597-89-000089\n")
# file.write("이수근 343-64-000064\n")
# file.write("박혁거세 136-97-000097\n")
# file.close()

print('----------')

# mode = 'r'
# account_list_read = []
# with open(path, mode, encoding='utf-8') as file:
#     lines = file.readlines()
#     for line in lines:
#         # print(line[-14:-1])
#         account_list_read.append(line[-14:-1])
# print(account_list_read)

# mode = 'r'
# account_list_read = []
# with open(path, mode, encoding='utf-8') as file:
#     lines = file.readlines()
#     for line in lines:
#         # 1. split() 함수 활용
#         name, num = line.split() # 기본값 공백 " "
#         account_list_read.append(num)
#         # # 2. strip() 함수 활용
#         # account_list_read.append(line[-14:].strip())
# print(account_list_read)

mode = 'r'
account_list_read = []
with open(path, mode, encoding='utf-8') as file:
    lines = file.readlines()
    for line in lines:
        # 1. split() 함수 활용
        # 특정 구분자 기준으로 문자영르 쪼개서 리스트(list)로 반환
        linelist = line.split() # 기본값 공백 " "
        # # 2. strip() 함수 활용
        # 양쪽 끝에 있는 공백이나 특정 문자를 제거
        account_list_read.append(linelist[1].strip())
print(account_list_read)

print('----------')

mode = 'r'
dict = {}
with open(path, mode, encoding='utf-8') as file:
    lines = file.readlines()
    for line in lines:
        # 1. split() 함수 활용
        # 특정 구분자 기준으로 문자영르 쪼개서 리스트(list)로 반환
        linelist = line.split() # 기본값 공백 " "
        # # 2. strip() 함수 활용
        # 양쪽 끝에 있는 공백이나 특정 문자를 제거
        dict[linelist[0]] = linelist[1].strip()
print(dict)

for key, val in dict.items():
    print(key, ":", val)

print('----------')

mode = 'a'
name_list2 = ["강호동","유재석"]
account_list2 = ["147-12-002093","146-22-102093"] 
with open(path, mode, encoding='utf-8') as file:
    for i in range(len(name_list2)):
        data = name_list2[i] + " " + account_list2[i] + "\n"
        file.write(data)
