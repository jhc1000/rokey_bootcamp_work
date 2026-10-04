# continue1.py

count = 0
while count < 3:
    count += 1
    if count == 3:
        continue
    print(count)
    
print("------------")
# 필터링 예제
# ""(빈값) / None 이면 건너뜀
# 유효한 데이터만 처리
users = ["admin", "guest", "", None, "user1", range(1), 1, 0]

for user in users:
    if not user: # False로 인식된 
        continue # ""(빈값), None 이면 건너뜀 
    print(user)

# 표현    자료형      의미
# ------------------------------------------
# ""      str         비어있는 문자열
# None    Nonetype    값이 없음을 나타내는 특별한 값


# False로 평가되는 경우
# if True/False:
#     pass

# False
# None
# 0       
# 0.0
# ""
# []
# ()
# {}
# 내용이 없는 객체 range(0)

print(bool(range(0)))
