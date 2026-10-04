# raise1.py

# raise 예외클래스명(예외정보데이터)
print("raise1")
try:
    raise NameError("HiThere")
except NameError:
    print("An exception flew by!")
print("exit")

# 비정상종료 -> 정상종료

# 주요 사용 이유
# - 잘못된 값 들어왔을 때 방지
# - 함수에서 조건을 위반 시 일단 중단
# - 사용자 정의 에러 처리

# 예) 은행 잔고 부족시 예외 발생

# 사용자 정의 에러클래스
class InsufficientBalanceError(Exception):
    pass

class Account:      # 계좌
    def __init__(self, balance):
        self.balance = balance
    def withdraw(self, amount): # 인출하기
        if amount > self.balance:   # 잔고 부족 상황
            raise InsufficientBalanceError("잔고 부족.")
        self.balance -= amount  # 잔고 부족 x 일때 
        return self.balance
    
my_account = Account(1000)
try:
    print(my_account.withdraw(1500))
except InsufficientBalanceError as e:
    print("출금 실패:", e)