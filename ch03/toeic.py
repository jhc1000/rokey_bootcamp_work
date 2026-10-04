# toeic.py

# print('--------')
# tscore = 700
# # tscore = 800
# # tscore = 950
# if tscore > 900:
#     print("당신의 토익 점수는", tscore, "상위권 점수입니다.")
# elif tscore > 700:
#     print("당신의 토익 점수는", tscore, "중위권 점수입니다.")
# else:
#     print("당신의 토익 점수는", tscore, "하위권 점수입니다.")
# print("if 문 종료됨")

print('--------')
# 토익 점수를 4분류 하는 프로그램
# 900 이상 : 상위권
# 900 미만 ~ 600이상 : 중상위권
# 600 미만 ~ 300이상 : 중위권
# 300 미만 : 하위권

tscore = 700
print("당신의 토익 점수는", tscore)
if tscore >= 900:
    print("상위권 점수입니다.")
elif tscore >= 600:
    print("중상위권 점수입니다.")
elif tscore >= 300:
    print("중위권 점수입니다.")
else:
    print("하위권 점수입니다.")
print("if 문 종료됨")

print(900 > (tscore >= 600) )
