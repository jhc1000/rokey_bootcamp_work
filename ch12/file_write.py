# file_write.py

# f = open(r"ch12\file1.txt", 'w')
f = open(r"ch12\file1.txt", 'w', encoding="utf-8")
# f = open(r"ch12\file1.txt", 'w', encoding="cp949")


# f.write("1번째 줄입니다.")
for i in range(1,11):
    data = "%d번째 줄입니다.\n" % i     # % 서식문자
    f.write(data)                       # %d 10진수 

# 파이썬은 cp949
# vscode는 utf-8

f.close()

# 메모장은 상황에 따라 디코딩을 한다