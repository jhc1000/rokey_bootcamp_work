# file_with.py

path = "./ch12/file2.txt"
mode = 'w'
# f = open(path, 'a',
#          encoding='utf-8')
with open(path, mode, encoding='utf-8') as f:
    # 파일에 내용 추가
    num = f.write("No pain, no gain.")
    print(num)

print('----------')

# f.close()