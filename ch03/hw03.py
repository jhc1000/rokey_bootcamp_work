# hw03.py

# #2
# print(3 == 5)

# print('------')

# #3
# print ((3 == 3) and (4 != 3))

# print('------')

# #4
# if 4 < 3:
#       print("Hello World.")
# else:
#       print("Hi, there.")

# print('------')

# #5
# if True :
#       if False:
#           print("1")
#           print("2")
#       else:
#           print("3")
# else :
#       print("4")
# print("5")

# print('------')

# #6
# na = int(input("숫자 하나 입력(ex:5) : "))
# if na % 2 == 0:
#     print(na, "는 짝수")
# else:
#     print(na, "는 홀수")
    
# print('-------')

# #7
# na = int(input("숫자 하나 입력(ex:255) : "))
# nb = na + 20
# limit = 255
# if na > limit and nb > limit:
#     print(limit)
# else:
#     print(nb)

# print('-------')

# #8
# na = int(input("숫자 하나 입력(ex:255) : "))
# nb = na - 20
# up_limit = 255
# down_limit = 0
# if nb > up_limit:
#     print(up_limit)
# elif nb < down_limit:
#     print(down_limit)
# else:
#     print(nb)
    
# print('-------')

# #9
# na = input("현재 시간 입력(ex: 02:00) : ")
# hour = int(na[0:2])
# min = int(na[3:5])
# print("현재시간:", na)
# if min % 60 == 0:
#     print("정각 입니다.")
# else:
#     print("정각이 아닙니다.")

#10
score = int(input("점수를 입력(ex: 83) : "))
print("score:", score)
if score > 80:
    print("grade is", "A")
elif score > 60:
    print("grade is", "B")
elif score > 40:
    print("grade is", "C")
elif score > 20:
    print("grade is", "D")
elif score > 0:
    print("grade is", "E")
else:
    print("점수를 제대로 입력하세요.")
    
print('-------')
