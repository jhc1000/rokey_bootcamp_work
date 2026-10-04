# Animal.py

## 클래스 : 동물
# 객체 : 고양이, 사자, 개, 사람, 호랑이, ...
# 속성 : 명칭, 나이, 무게, 번식형태(알/새끼), 
# 기능/동작 :  먹다, 자다, 이동하다, 소리내다, 싸우다, ...
class Animal:
    def __init__(self, age, weight):
        self.age = age
        self.weight = weight

    def eat(self):
        print("먹다")
    def move(self):
        print("이동하다")
    def sound(self):
        print("소리내다")

## 클래스 : 고양이
# 객체 : 나비, 야옹이, 뽀글이, 뽀삐, ...
# 속성 : 명칭, 나이, 무게, 색상, 번식형태(알/새끼), 
# 기능/동작 :  먹다, 자다, 이동하다, 소리내다, 싸우다, 할퀴다, ...
class Cat(Animal):
    def __init__(self, age, weight, color):
        super().__init__(age, weight)
        self.color = color
    def eat(self):
        print("잡식하다")
    def sound(self):
        print("야옹~ ", end="")
        super().sound()
    def scratch(self, object):
        print(object, "을/를 할퀴다")

class Tiger(Animal):
    def eat(self):
        print("육식하다")
    def sound(self):
        print("어흥! ", end="")
        super().sound()

if __name__ == "__main__":
    cat1 = Cat(3, 10, "검은색")
    print(cat1.age, cat1.weight, cat1.color)
    cat1.eat()
    cat1.move()
    cat1.sound()
    cat1.scratch("나")

    print('-----------')

    tiger1 = Tiger(5, 80)
    print(tiger1.weight)
    tiger1.eat()
    tiger1.move()
    tiger1.sound()


