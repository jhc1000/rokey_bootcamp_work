# hw10.py

# 5
class Phone:
    def __init__(self, number, color):
        self.number=number
        self.color=color

phone = Phone("010-1234-5678", "검정")
print(phone.number)
print(phone.color) 

print('-----------')

# 6,7
class SmartPhone(Phone):
    def __init__(self, number, color, company):
        super().__init__(number, color)
        self.company=company

apple = SmartPhone("010-1234-5678", "검정", "애플")
print(apple.number)
print(apple.color)
print(apple.company)

print('-----------')

# 8
class Phone:
    def __init__(self, number, color):
        self.number=number
        self.color=color
    def showInfo(self):
        print("전화번호:", self.number)
        print("색상:", self.color)
        
phone = Phone("010-1234-5678", "검정")
phone.showInfo()

print('-----------')

# 9,10
class SmartPhone(Phone):
    def __init__(self, number, color, company):
        super().__init__(number, color)
        self.company=company
    def showInfo(self):
        super().showInfo()
        print("회사:", self.company)

apple = SmartPhone("010-1234-5678", "검정", "애플")
apple.showInfo()


print('-----------')
