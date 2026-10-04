# file_readlines.py

path = "./ch12/file1.txt"
f = open(path, 'r',
         encoding='utf-8')
# f = open(path, 'r') # cp949로 디코딩 불가

# 파일 줄단위로 읽기
lines = f.readlines()
print(lines)
for line in lines:
    print(line, end="")
    # print(line) #\n 도 출력되서 한칸 씩 떨어짐

f.close()