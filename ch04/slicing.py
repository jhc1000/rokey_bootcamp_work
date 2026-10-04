# slicing.py

# 인덱싱
# 리스트명[인덱스]

# 슬라이싱
# 리스트명[start:stop] start ~ (stop-1) 번 까지

week = ['월', '화', '수', '목', '금', '토', '일']

print(week)

print(week[2])
print(week[3:7])
print(week[1:5])

print('----------')
# 인덱스 생략 가능:

# 1. 시작인덱스가 0인 경우
print(week[:5])
# 2. 마지막 데이터까지 접근하려는 경우
print(week[1:])
# 3. 모든 데이터에 접근하려는 경우
print(week[:])

print('----------')

# 리스트명[start:stop:step] 
# start :  시작 인덱스
# stop : 끝 인덱스(미포함)
# step : 이동 간격(생략가능:기본값 1)

week = ['월', '화', '수', '목', '금', '토', '일']
print(week[1:5])
print(week[1:5:1])
print(week[1:5:2])

print('음수 인덱싱----------')
print(week[-1])
print(week[-2])
print(week[-3])

print('음수 슬라이싱----------')
# 끝 인덱스가 포함되지 않는다
print(week[-3:-1])
print(week[-5:5])

# 범위 설정 규칙 : 좌 -> 우
print(week[-3:3]) # [] -3: 금, 3: 목 
print(week[6:5]) # []
print(week[-1:3:-1]) # 거꾸로 가는 형태

print(week[-4::-1]) # 거꾸로 가는 형태
