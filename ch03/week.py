# week.py
text = "오늘의 요일을 한글로 알려주세요.(ex:월요일)\n"
week = input(text)

if week == '월요일':
    print("오늘은", "monday")
elif week == '화요일':
    print("오늘은", "tuesday")
elif week == '수요일':
    print("오늘은", "wednesday")
elif week == '목요일':
    print("오늘은", "thursday")
elif week == '금요일':
    print("오늘은", "friday")
elif week == '토요일':
    print("오늘은", "saturday")
elif week == '일요일':
    print("오늘은", "sunday")
else:
    print("잘 못 입력했습니다.")