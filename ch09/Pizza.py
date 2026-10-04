# Pizza.py

# class 클래스명:
#     # pass
#     # 1. 멤버함수(=메서드)
#     def 멤버함수명(self, 매개1, 매개2):
#         코드블록
#         self.인스턴스멤버변수명 = 데이터값
#         return 반환값
#     # 2. 멤버변수
#     클래스멤버변수명 = 데이터값

class Pizzaclass:
    def order(self):
        print("주문하다.")
        self.kind = 10
    large = 21
    
## 객체 생성
# 객체변수명 = 클래스명()   # 생성자함수 (객체를 생성해주는)
pizza1 = Pizzaclass()


# 객체변수명.멤버함수명(인수)
# 객체변수명.멤버변수명
pizza1.order()          # 함수 호출
print(pizza1.kind)      # 변수 접근
print(pizza1.large)

print(106+200*0.2+181*0.1+171*0.05)