# re_search.py

# 패턴객체 = re.compile(메타문자를 활용한 정규표현식)
# 매치객체 = 패턴객체.search(패턴과 일치 여부를 확인할 문자열)

import re

p = re.compile("[a-z]+")
m = p.search("python")       # 'python'
m = p.search("3 python")     # 'python'
print(m)

print('---------')
p = re.compile("[a-z]+")
m = p.search("python")       # 'python'
m = p.search("3 python")     # 'python'
if m:
    print(f'search found: {m.group()}')
    print(f'start: {m.start()}')
    print(f'end: {m.end()}')
    print(f'span: {m.span()}')
else:
    print('No search')

print('---------')
# 검색대상 문자열 전체를 검색하지만, 반환되는 내용은 첫번째 검색된 내용만 포함
text = "The mission of the Python Software Foundation is to promote, protect, and advance the Python programming language, and to support and facilitate the growth of a diverse and international community of Python programmers."
p = re.compile("Python")
m = p.search(text)     
print(m)    # <re.Match object; span=(19, 25), match='Python'>

# 처음 나온 Python 이 검색되서 나옴.