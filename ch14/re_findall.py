# re_findall.py

# 패턴객체 = re.compile(메타문자를 활용한 정규표현식)
# 리스트 = 패턴객체.findall(패턴과 일치 여부를 확인할 문자열)

import re
# 일치하는 패턴을 모아서 리스트로 반환
text = "The mission of the Python Software Foundation is to promote, protect, and advance the Python programming language, and to support and facilitate the growth of a diverse and international community of Python programmers."
p = re.compile("Python")
result = p.findall(text)     
print(result, len(result))    # ['Python', 'Python', 'Python']

print('---------')
p = re.compile("[a-z]+")
result = p.findall("life is too short")
result = p.findall("life\nis\ttoo8short!")
print(result, len(result))

print('---------')
# p = re.compile("\w") # 한글도 포함됌
p = re.compile("[가-힝]+")
result = p.findall("동해물과 백두산이 마르고 닳도록")
print(result, len(result))