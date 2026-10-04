# default1.py

def person_a(width, height):
    print("디폴트값 없음")
    print("width:", width, "height:", height)

def person_b(width=13, height=25):
    print("디폴트값 있음")
    print("width:", width, "height:", height)

# 시도1. 함수 오버로딩 지원안함 -> 실패!
def person_a():
    print("매개변수 없는 함수")
    
# 시도2. 기본 매개변수 활용 -> 성공!
def person_a(width=2, height=5):
    print("디폴트값 있음")
    print("width:", width, "height:", height)
    
person_a(10, 20)
person_a()
person_b(10, 20)
person_b()

print('----------')
