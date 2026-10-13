# re_finditer.py

# 패턴객체 = re.compile(메타문자를 활용한 정규표현식)
# iterator = 패턴객체.finditer(패턴과 일치 여부를 확인할 문자열)

# finditer()  함수는 매치객체를 요소로하는 이터레이터 형태로 반환
import re
# 일치하는 패턴을 모아서 매치객체들을 이터레이터로 모아서 반환
text = "The mission of the Python Software Foundation is to promote, protect, and advance the Python programming language, and to support and facilitate the growth of a diverse and international community of Python programmers."
p = re.compile("Python")
result = p.finditer(text)   
# print(list(result))  
for r in result: print(f"{r.group()} / {r.span()}") 

print('---------')
p = re.compile("[a-z]+")
result = p.finditer("life is too short")
# result = p.finditer("life\nis\ttoo8short!")
# print(list(result))
for r in result: print(f"{r.group()} / {r.span()}") 

print('---------')
# p = re.compile("\w") # 한글도 포함됌
p = re.compile("[가-힝]+")
result = p.finditer("동해물과 백두산이 마르고 닳도록")
# print(list(result))
for r in result: print(f"{r.group()} / {r.span()}") 