# Human.py

class Human:
    # 1. 멤버변수
    eye = 2
    nose = 1
    mooth = 1
    
    def __init__(self, age, name):
        self.age = age
        self.name = name
    def intro(self):
        print(str(self.age) + " 살 " + self.name + "입니다.")

print(Human.eye)
print(Human.nose)
print(Human.mooth)

kim = Human(29, "김상형")
# print(kim.name)
# print(kim.age)
kim.intro()
lee = Human(45, "이승우")
# print(lee.name)
# print(lee.age)
lee.intro()
