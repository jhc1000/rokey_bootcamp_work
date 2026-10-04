# print_string.py

# 문자열 출력 방식
### 다양한 문자열 사용(출력) 방법

# 표준 출력 함수 : print(인수) 활용
# 1. 기능: 인수를 모니터 출력
# 2. 인수: 객체(다양한 자료형 모두)
# 3. 반환값: 없음(None)

name = '홍길동'
age = 700
height = 191.3

# 기본 형식
# 1. print("내용1", "내용2")
print("이름:", name, "나이:", age, "신장:", height)

# 2. % 연산자 사용 방식
# 서식문자 활용 -> %s: 문자열, %d: 10진수, %f: 실수형, %x: 16진수
data = "%d번째 줄입니다.\n" % (2)
print(data)
print("이름: %s 나이: %d 신장: %f.1" % (name, age, height))

# 3. format() 메서드 활용
# {} 와 format() 사용해서 출력하는 형태
# "{}".format(인수)
print("이름: {} 나이: {} 신장: {}".format(name, age, height))

# 4. f-string 사용 방식
print(f"이름: {name} 나이: {age} 신장: {height:.1f}")
