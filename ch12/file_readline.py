# file_readline.py

path = "./ch12/file1.txt"
f = open(path, 'r',
         encoding='utf-8')
# f = open(path, 'r') # cp949로 디코딩 불가

# 파일 줄 1개 읽기
line = f.readline()
# line = f.readline(4)
print(line)


f.close()


# (method) def readline(
#     size: int = -1,
#     /       # 위치인수만 사용 가능
# ) -> str