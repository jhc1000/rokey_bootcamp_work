# dup_for.py
# 중첩 for문

# for 변수 in 리스트:
#     코드블록
#     for 변수 in 리스트:
#         코드블록

# for 변수 in 리스트:
#     코드블록
# for 변수 in 리스트:
#     코드블록

# 2차원 형태 표현
for j in range(5):      # 0 1 2 3 4
    print(j, end=" ")
    for i in range(10):    # 0 1 2 3 4 5 6 7 8 9
        print("*", end="")
    print()
    

# 0 **********
# 1 **********
# 2 **********
# 3 **********
# 4 **********