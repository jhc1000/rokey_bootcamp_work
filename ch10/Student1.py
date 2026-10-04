# Student.py

## 클래스 정의 : Human
# 객체 : lee, kim, ...
# 속성 : 이름, 나이, 직업, 눈, 코, 입, ...
# 기능/동작 : 자기소개, 자다, 먹다, 말하다
class Human:
    # 1. 멤버변수
    eye = 2
    nose = 1
    mooth = 1
    def __init__(self, name, age):
        self.age = age
        self.name = name
    def intro(self):
        print(self.age, "살", self.name, "입니다.")
    def eat(self, food: str):
        print(food, '먹다')
    def sleep(self):
        print('자다')
    def talk(self):
        print('말하다')

## 클래스 정의 : Human
# 객체 : lee, kim, ...
# 속성 : 이름, 나이, 직업, 눈, 코, 입, ...
# 기능/동작 : 자기소개, 자다, 먹다, 말하다, 공부하다
class Student(Human):
    def __init__(self, name, age, studentNum):
        self.name = name
        self.age = age
        self.studentNum = studentNum
    def intro(self):    # 자식클래스 멤버 우선순위가 높다
        print(self.studentNum, "학번", self.age, "살", self.name, "입니다.")
    def study(self):
        print('공부하다')
    def exam(self):
        print("시험을 보다")

if __name__ == "__main__":
    print("눈 개수:", Human.eye)
    lee = Human("이수근", 49)
    lee.intro()
    lee.eat("치킨")

    print('----------')

    kim = Student("김기태", 29, 20260929)
    print(kim.studentNum) # 자식 속성
    kim.intro()           # 자식 메서드 오버라이딩
    kim.sleep()           # 부모 메서드 상속
    kim.exam()            # 자식 메서드