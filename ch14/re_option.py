# re_option.py

import re

# 옵션 외울 필요 없음. 찾아서 써라.

# DOTALL, S  : (고정 상수 값)
# .(dot) 이 줄바꿈 문자를 포함해 모든 문자와 매치 될 수 있게 해줌
p = re.compile("a.b")
print(p.match("a\nb"))

p = re.compile("a.b", re.DOTALL)
print(p.match("a\nb"))

p = re.compile("a.b", re.S)
print(p.match("a\nb"))

print('---------')
# IGNORECASE, I : 대소문자 관계없이 매치 될 수 있게 해줌
p = re.compile("[a-z]+")
print(p.match("python"))
print(p.match("Python"))
print(p.match("PYTHON"))

p = re.compile("[a-z]+", re.IGNORECASE)
print(p.match("python"))
print(p.match("Python"))
print(p.match("PYTHON"))

p = re.compile("[a-z]+", re.I)
print(p.match("python"))
print(p.match("Python"))
print(p.match("PYTHON"))

print('---------')
# MULTILINE, M : 여러 줄과 매치될 수 있게 한다 (^, $)
p = re.compile("^python\s\w+")     # ^ 문자열시작, \s 공백문자, \w, + 1번이상 반복
data = """python one
life is too short
python two
life three
you need python
python three"""
print(p.findall(data))

p = re.compile("^python\s\w+", re.MULTILINE)     # ^ 문자열시작, \s 공백문자, \w, + 1번이상 반복
data = """python one
life is too short
python two
life three
you need python
python three"""
print(p.findall(data))

p = re.compile("^python\s\w+", re.M)     # ^ 문자열시작, \s 공백문자, \w, + 1번이상 반복
data = """python one
life is too short
python two
life three
you need python
python three"""
print(p.findall(data))

print('---------')
# VERBOSE, X : verbose 모드 사용. 정규식을 보기 편하게 만들 수 있고 주석/ 개행 등 사용가능
p = re.compile(r'&[#](0[0-7]+|[0-9]+|x[0-9a-fA-F]+);')
p= re.compile(r"""
              &[#]            # Start of a numeric entity reference
              (
              0[0-7]+         # Octal form(8진수 형식)
              |[0-9]+         # Decimal form(10진수 형식)     # | : or 기호
              |x[0-9a-fA-F]+  # Hexadecimal form(16진수 형식)
              )               # 후행 semicolon
              ;""",
              re.VERBOSE)

# HTML/XML 문자 참조
data = "&#07; &#8; &#x0A;"      # 8진수, 10진수, 16진수
print(p.findall(data))