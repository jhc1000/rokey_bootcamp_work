# Singer.py

## 클래스 정의
# 속성 : 이름, 성별, ...
# 동작/기능 : 노래하기, 춤추기, ...
class Singer:
    # 1. 멤버변수(클래스/인스턴스)
    # 클래스 멤버변수 
    # 변수명 = 값
    iu_name = "아이유"
    bts_name = "BTS"
    
     # 2. 메서드 -> 동작
    # def 함수명(self):
    #     코드블록
    #     self.변수명 = 값
    def sing(self):
        print(self.song)
        # 인스턴스 멤버 변수
        self.gender1 = "여자"
        self.gender2 = "남자"

# 클래스 멤버변수 접근 : 클래스명.멤버변수명
print(Singer.iu_name)
print(Singer.bts_name)

## 객체 정의
iu = Singer()
bts = Singer()

iu.song = "이 밤 그날의 반딧불을 당신의 창 가까이 보낼게요~"
bts.song = "Dynamite"

## 객체 멤버 접근
iu.sing()
print(iu.iu_name)
print(iu.gender1)   # 인스턴스 변수 : 객체명.멤버변수명

bts.sing()
print(bts.bts_name)
print(bts.gender2)

bts.bts_name = "비티에스"
bts.sing()
print(bts.bts_name)
print(bts.gender2)


# class 자동차:
#     모양 = 32
#     크기 = 32
#     def 차량1(self):
#         self.색1 = "빨"
        
#     def 차량2(self):
#         self.색2 = "주"