# re_match.py

# 패턴객체 = re.compile(메타문자를 활용한 정규표현식)
# 매치객체 = 패턴객체.match(패턴과 일치 여부를 확인할 문자열)

# class 클래스명:
#     def match(self):
#         return 매치객체
#     def search(self):
#         return 매치객체
#     ...
# def 함수명():
#     코드블록 
#     패턴객체 = 클래스명()
#     return 패턴객체

import re

p = re.compile("[a-z]+")
m = p.match("python")       # 'python'
# m = p.match("3 python")   # None
print(m)

print('---------')
p = re.compile("[a-z0-9]+")
m = p.match("3 python")     # '3'
m = p.match("3python")      # '3python'
print(m)

print('---------')
p = re.compile("[a-z]+")
m = p.match("python")               # 'python'
m = p.match("python invent")        # 'python'
if m:
    print(f'Match found: {m.group()}')
    print(f'start: {m.start()}')
    print(f'end: {m.end()}')
    print(f'span: {m.span()}')
else:
    print('No match')

# m.group() : 매치된 str를 반환
# m.start() : 매치 시작
# m.end() : 매치 끝
# m.span() : 매치 범위