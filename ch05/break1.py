# break1.py
# 반복을 종료

count = 0
while count < 3:
    count = count + 1
    if count == 3:
        break
    print(count)
print("while문 종료")

print('-----------')
users = ["kim", "lee", "park"]

for user in users:
    print(user)
    if user == "lee":
        print("발견!")
        break

 
# 찾으면 탐색 중지 => 성능 절약