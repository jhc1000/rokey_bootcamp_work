# generator1.py

# 제너레이터 생성 방법
# 2. 제너레이터 표현식 활용: 제너레이터 컴프리핸션
gen = (i*i for i in range(1,100))
print(type(gen))
print(gen)
for item in gen:
    print(item)
# print(next(gen))


