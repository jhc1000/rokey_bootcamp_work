# priority.py

# 연산자 우선순위
# 괄호 > 산술 > 비교 > 논리 > 대입
# 산술 우선순위 : ** > +x, -x > *, /, //, % > +, - 
# 논리 우선순위 : not > and > or 
# 비교 우선순위 : 같은 우선순위
print( 2 * (3 - 5) )

print('---------')
print(9 > 4 and 3 > 2) # T
# print(True and True)
print(9 < 4 and 3 > 2) # F
print(9 < 3 or 3 < 2) # F
print(9 < 4 or 3 > 2) # T

print('---------')
print((3 - 5) < 1) # -2 < 1 True
print(3 - 5 < 1) # -2 < 1 True
print(3 - 5 < 1 and 3 - 5 > 1) # True and False False