# Cadd.py

class Cadd:
    def fadd(self, a, b):
        # x1 = a
        self.x = a
        self.y = b
        self.hap = self.x+self.y

obj = Cadd()
obj.fadd(10, 20)
print("객체 obj 내의 인스턴스 변수 x 값:", obj.x)
print("객체 obj 내의 인스턴스 변수 x 값:", obj.y)
print("객체 obj 내의 인스턴스 변수 hap 값:", obj.hap)

# print("객체 obj 내의 지역 변수 x1 값:", x1)

# 메서드 실행 중에만 필요 -> 지역변수
# 객체가 계속 기억해야 함 -> 인스턴스 변수
# 모든 객체가 공유해야 함 -> 클래스 변수