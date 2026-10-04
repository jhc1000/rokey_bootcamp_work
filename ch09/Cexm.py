# Cexm.py

class Cexm:
    def fsam(self):
        print("멥버함수(메서드)")
    def fsbm(self, pa):
        self.x = pa
        print("멤버변수 x는", self.x)


ca = Cexm()
ca.fsam()
ca.fsbm(19)

cb = Cexm()
cb.fsam()
cb.fsbm(123)
