# Bag.py

## 클래스 정의 : 가방
# 객체 : 에코백, 핸드백, 백팩, 크로스백
# 속성 : 제조사, 색상, 가격, 재질
# 동작/기능 : 넣다, 빼다, 매다, 주머니에 넣다, 지퍼를 닫다, ...
class Bag:
    # 1. 멤버변수(속성, 명사)
    call_name = '가방'
    
    # 스폐셜 메소드 : 클래스 초기화 시 필요한 데이터 및 기능을 추가 가능
    # 각 객체의 메모리 공간에 추가
    def __init__(self, name, color):     
        self.data = []
        self.name = name
        self.color = color

    # 2. 메서드(기능/동작, 동사)
    def add(self, x):
        print(x, "넣다")
        self.data.append(x)
        
    def open(self):
        print(self.name, "열다")
    
    def close(self):
        print(self.name, "닫다")
    
    def remove(self, x):
        print(x, "꺼내다")
        self.data.remove(x)
        
    def addtwice(self, x):
        print(x, "두번 넣다")
        self.add(x)
        self.add(x)
        # self.data.append(x)
        # self.data.append(x)

eco_bag = Bag("에코", "녹색")
print(eco_bag.call_name)
print(eco_bag.name)
print(eco_bag.color)
eco_bag.add("생수")
eco_bag.add("과자")
eco_bag.remove("생수")
# print(Bag.data)
print(eco_bag.data)

print('------------')

hand_bag = Bag("핸드", "검정")
print(hand_bag.call_name)
print(hand_bag.name)
print(hand_bag.color)
hand_bag.add("휴대폰")
hand_bag.add("화장품")
hand_bag.add("이어폰")
hand_bag.remove("휴대폰")
print(hand_bag.data)

print('------------')
# 실습 : 새 가방 객체를 하나 생성하고 물건 담아보기(두번 담기 기능 추가)
backpack = Bag("배낭", "국방")
print(backpack.call_name)
print(backpack.name)
print(backpack.color)
backpack.add("노트북")
backpack.add("손수건")
backpack.addtwice("책")
backpack.remove("책")
print(backpack.data)
