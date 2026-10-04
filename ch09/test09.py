# test09.py

def fadd(a=1, b=2):
    return a+b

ohap = fadd(10,20)
print("ohap:", ohap)

ohap2 = fadd(10)
print("ohap2:", ohap2)

ohap3 = fadd()
print("ohap3:", ohap3)

print('----------')

class Cadd:
    def fadd(self, a=1, b=2):
        self.x = a
        self.y = b
        self.hap=self.x+self.y
        
obj=Cadd()
obj.fadd(10,20)
print(obj.hap)
obj.fadd(10)
print(obj.hap)
obj.fadd()
print(obj.hap)

print('----------')

class Animal:
    def __init__(self, name):
        self.name=name
    def sound(self, sound):
        print(sound, "소리내다")

cat = Animal('고양이')
print('이름(name)=', cat.name)
cat.sound('야옹')

print('----------')


class Fruit:
    def __init__(self, name, color):
        self.name=name
        self.color=color
    def taste(self, taste):
        print(taste, "맛이나다")
        
orange=Fruit('오렌지','노란색')
print('이름=',orange.name,'색상=',orange.color)
orange.taste('새콤하다')
