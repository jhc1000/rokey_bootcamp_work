# file_read.py

path = "./ch12/file1.txt"
f = open(path, 'r',
         encoding='utf-8')
# f = open(path, 'r') # cp949로 디코딩 불가

data = f.read()
print(data)
print(repr(data)) # 이스케이프 문자 (\n) 까지 출력
f.close()