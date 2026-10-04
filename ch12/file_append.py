# file_append.py

path = "./ch12/file1.txt"
f = open(path, 'a',
         encoding='utf-8')
# f = open(path, 'r') # cp949로 디코딩 불가

# 파일에 내용 추가
for i in range(11, 21):
    data = "%d 번째 줄입니다.\n"%i
    f.write(data)

f.close()

