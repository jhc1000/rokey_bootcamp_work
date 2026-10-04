# hw09.py

# 3
class Phone:
    pass

print('----------')
# 4
class Phone:
    pass

my_phone=Phone()

print('----------')
# 5
class Phone:
    def __init__(self):
        print("휴대폰 생성")


print('----------')        
# 6
class Phone:
    def __init__(self, company, year, color):
        print("휴대폰 생성")

print('----------')
        
# 7 
class Phone:
    def __init__(self, company, year, color):
        print("휴대폰 생성")
        self.company = company
        self.year = year
        self.color = color

my_phone=Phone('삼성', 2026, '흰색')
print(my_phone.company)
print(my_phone.year)
print(my_phone.color)

print('----------')

# 8
class Phone:
    def __init__(self, company, year, color):
        print("휴대폰 생성")
        self.company = company
        self.year = year
        self.color = color
    def info(self):
        print(self.company)
        print(self.year)
        print(self.color)

my_phone=Phone('삼성', 2026, '흰색')
print(my_phone.company)
print(my_phone.year)
print(my_phone.color)
my_phone.info()

print('----------')

# 9
class Phone:
    def __init__(self, company, year, color):
        print("휴대폰 생성")
        self.company = company
        self.year = year
        self.color = color
    def info(self):
        print(self.company)
        print(self.year)
        print(self.color)
    def sefInfo(self, company, year, color):
        self.company = company
        self.year = year
        self.color = color

my_phone=Phone('삼성', 2026, '흰색')
print(my_phone.company)
print(my_phone.year)
print(my_phone.color)
my_phone.info()
my_phone.sefInfo('애플', 2025, '검은색')
my_phone.info()
print('----------')