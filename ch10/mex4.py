# mex1.py
print("mex4.py")
print(__name__)

class Cvalue:
    def __init__(self):
        self.lista = []
    def add(self, num):
        self.lista.append(num)
    def fprint(self):
        print(self.lista)

def plus(a, b):
    c = a + b
    return c

if __name__ == "__main__":
    # 변수
    p1=Cvalue()
    p1.add(1)
    p1.add(2)
    p1.add(3)
    p1.fprint()
    print(plus(10,20))