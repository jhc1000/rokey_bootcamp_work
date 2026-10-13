# re_module.py

# 정규표현식(Regular Expression)
# : 문자열 패턴을 정의해서 
# 검색, 검사, 치환, 추출 등을 할 수 있도록 해주는 
# 문자열 처리 규칙

import re 

# 정규표현식을 정의해서 컴파일 함수의 인수로 전달하면 
# 패턴 객체를 반환함.
# 패턴객체: "검색대상문자열"에서 패턴의 발견을 도와주는 객체
# match 함수: 문자열 처음부터 확인하여 정규식과 매치되는지 조사 

# 패턴객체 = re.compile("정규표현식")
# 매치객체 = 패턴객체.match("검색대상문자열")
# print(매치객체)


# 메타 문자: 별도의 의미가 담겨있는 문자

# [] 문자
# 1. [] 사이의 문자들과 매칭
# - 일반문자: [] 내 한개의 문자와 매치
# - 메타문자: 특수한 기능 없이 사용. (단, 일부는 예외)
# - 도트(.), + 는 문자 자체 인식
# - 역슬래시(\) 뒤에 쓰인 메타문자 -> 문자 자체로 인식, [\^]
# - 예외 경우
#     캐럿(^): 맨앞에 위치한 경우 -> 부정(not), [^a-z]
#     하이픈(-): 범위 표시, [a=z], [0-9], [A-Z] 두 문자 사이의 범위를 의미
# - 별도 표기법 활용
# \d : 숫자와 매치, [0-9]
# \D : 숫자 아닌 것과 매치, [^0-9]
# \s : 화이트스페이스(whilespace) 문자와 매치, [ \t\n\r\f\v]
# \S : 화이트스페이스 아닌 것과 매치, [^ \t\\r\f\v]
# \w : 문자+숫자 와 매치, [a-zA-Z0-9_]
# \W : 문자+숫자 아닌 문자와 매치, [^a-zA-Z0-9_]

# p1 = re.compile("a")  # <re.Match object; span=(0, 1), match='a'>
p1 = re.compile("ab")   # None
m1 = p1.match("apple")
print(m1) 

p1 = re.compile("b")
m1 = p1.match("apple")
print(m1)   # None

p1 = re.compile("p")
m1 = p1.match("apple")
print(m1)   # None

p1 = re.compile("ap")
m1 = p1.match("apple")
print(m1)   # None

print('-----------')
# p1 = re.compile("[a]")
p1 = re.compile("[ab]")
# m1 = p1.match("apple")
m1 = p1.match("banana")     # <re.Match object; span=(0, 1), match='b'>
print(m1)   # <re.Match object; span=(0, 1), match='a'>

print('-----------')
p = re.compile("[abc]")     # a or b or c
print(p.match("a"))         # 'a'
print(p.match("before"))    # 'b'
print(p.match("dude"))      # None
print(p.match("format"))    # None

# 반환: 매치객체 -> 문자열과 패턴 일치
# 반환: None -> 문자열과 패턴 불일치 

print('-----------')
p = re.compile("[ab0c]")
print(p.match("apple"))     # a
print(p.match("banana"))    # b
print(p.match("0dude"))     # 0

print('하이픈(-)-----------') # 범위 의미
p = re.compile("[a-c]")
print(p.match("apple"))         # a
print(p.match("banana"))        # b
print(p.match("watermelon"))    # None
print(p.match("-watermelon"))   # None
print(p.search("format"))

p = re.compile("[0-5]")
print(p.match("1:apple"))         # 1
print(p.match("2:banana"))        # 2
print(p.match("7:watermelon"))    # None

p = re.compile("[a-zA-Z]")  # 모든 알파벳
print(p.match("apple"))         # a
print(p.match("Banana"))        # b
print(p.match("watermelon"))    # w


print('캐럿(^)-----------') # 부정 의미
p = re.compile("[^a-c]")    # not [abc]
print(p.match("apple"))         # None
print(p.match("banana"))        # None
print(p.match("watermelon"))    # w

print('역슬래시(\)-----------') # 의미있는 문자 -> 없는 문자
p = re.compile("[\^a-c]")    # ^ or a or b or c
print(p.match("apple"))         # a
print(p.match("^apple"))        # ^
print(p.match("banana"))        # b
print(p.match("watermelon"))    # None

print('-----------')
p = re.compile("[\^a\-c]")    # ^ or a or - or c
print(p.match("apple"))         # a
print(p.match("^apple"))        # ^
print(p.match("banana"))        # None
print(p.match("-banana"))       # -
print(p.match("watermelon"))    # None

print('별도 표기법-----------') 
p = re.compile("\d")    # [0-9]
# p = re.compile("\D")    # [^0-9]
print(p.match("1:apple"))         # 1   -> None
print(p.match("banana"))          # None -> b
print(p.match("7:watermelon"))    # 7   -> None

print('-----------')
p = re.compile("\s")    # [ \t\n\r\f\v]
# p = re.compile("\S")    # [^ \t\n\r\f\v]
print(p.match(" apple"))          # ' ' -> None
print(p.match("\tbanana"))        # '\t' -> None
print(p.match("\nwatermelon"))    # '\n' -> None

print('-----------')
p = re.compile("\w")    # [a-zA-Z0-9_]
# p = re.compile("\W")    # [^a-zA-Z0-9_]
print(p.match("1apple"))   # 1 -> None
print(p.match("Banana"))   # B -> None
print(p.match("melon"))    # m -> None
print(p.match("_orange"))  # _ -> None

# . 문자
print('도트(.)-----------')
# p = re.compile(".")
p = re.compile("..")
print(p.match("apple"))     # 'a'   
print(p.match("2apple"))    # '2'
print(p.match("\napple"))   # None
print(p.match("+apple"))    # '+'
print(p.match(".apple"))    # '.'

print('-----------')
p = re.compile("a.b")
print(p.match("aab"))       # 'aab'   
print(p.match("a0b"))       # 'a0b'
print(p.match("abc"))       # None

print(p.match("a000b"))     # None
print(p.match("a\nb"))      # None
print(p.match("a\tb"))      # 'a\tb''

print('-----------')
p = re.compile("a[.]b")
p = re.compile("a\.b")
print(p.match("a.b"))       # 'a.b'  
print(p.match("aab"))       # None  
print(p.match("a0b"))       # None
print(p.match("abc"))       # None
print(p.match("a000b"))     # None
print(p.match("a\nb"))      # None
print(p.match("a\tb"))      # None

# * 문자
print('반복(*)-----------')
p = re.compile("a*")
print(p.match("apple"))     # 'a'   
print(p.match("pple"))      # ''
print(p.match("aaapple"))   # 'aaa'

print('-----------')
p = re.compile("ca*t")
print(p.match("ct"))        # 'ct'   
print(p.match("cat"))       # 'cat'
print(p.match("caaaat"))    # 'caaaat'
print(p.match("cbt"))       # None
print(p.match("c t"))       # None

print('-----------')
p = re.compile("a*b*c")
print(p.match("abc"))           # 'abc'   
print(p.match("aaabbc"))        # 'aaabbc'
print(p.match("bbbbcccc"))      # 'bbbc'
print(p.match("ccc"))           # 'c'

# + 문자
print('반복(+)-----------')
p = re.compile("ca+t")
print(p.match("ct"))        # None
print(p.match("cat"))       # 'cat'
print(p.match("caaaat"))    # 'caaaat'
print(p.match("cbt"))       # None
print(p.match("c t"))       # None

# {} 문자
print(r'반복횟수제한({})-----------')
p = re.compile("ca{2}t")
print(p.match("ct"))            # None
print(p.match("cat"))           # None
print(p.match("caat"))          # 'caat'
print(p.match("caaat"))         # None
print(p.match("caaaat"))        # None

print('-----------')
p = re.compile("ca{2,5}t")
print(p.match("ct"))            # None
print(p.match("cat"))           # None
print(p.match("caat"))          # 'caat'
print(p.match("caaat"))         # 'caaat'
print(p.match("caaaat"))        # 'caaaat'

print('-----------')
p = re.compile("ca{,1}t")       # 0도 포함
print(p.match("ct"))        # 'ct'
print(p.match("cat"))       # 'cat'
print(p.match("caat"))      # None

print('-----------')
p = re.compile("ca{1,}t")
print(p.match("ct"))        # None
print(p.match("cat"))       # 'cat'
print(p.match("caat"))      # 'caat'

print('-----------')
p = re.compile("ca{0,}t")
print(p.match("ct"))        # 'ct'
print(p.match("cat"))       # 'cat'
print(p.match("caat"))      # 'caat'

# ? 문자
print(r'?(={0,1})-----------')
p = re.compile("ca?t")
# p = re.compile("ca{0,1}t")
print(p.match("ct"))        # 'ct'
print(p.match("cat"))       # 'cat'
print(p.match("caat"))      # None

# ^ 캐럿 문자
print('문자열시작(^)-----------')
p = re.compile("^hello")
print(p.match("hello world!"))       # 'hello'
print(p.match(" hello world!"))      # None
print(p.match("\nhello_world!"))     # None
print(p.match("pello_world!"))     # None

print('-----------')
p = re.compile("[^hello]")      # not (h or e or l or o)
print(p.match("hello world!"))       # None
print(p.match(" hello world!"))      # " "
print(p.match("\nhello_world!"))     # "\n"
print(p.match("pello_world!"))       # "p"

# $ 캐럿 문자
print('문자열끝($)-----------')
p = re.compile("world$")
print(p.match("world"))                 # 'world'
print(p.match("hello world"))           # None      match 특성상 맨앞부터 맞아야 된다.
print(p.match(" hello world!"))         # None
print(p.match("world\n"))               # 'world'
print(p.search("hello world\n"))        # None
print(p.match("\nhello_world "))        # None
print(p.match("world hello world"))     # None

# p.match(): 문자열의 시작 부분부터 패턴과 일치하는지 확인
# 주의! world 뒤에 \n 이 있지만 
# $ 메타문자는 마지막 줄바꿈 바로 앞을 문자열의 끝 처럼 인식

# p.search(): 문자열 전체를 검색하여 패턴과 일치하는지 확인
print('p.search()-----------')
p = re.compile("world$")
print(p.search("world"))                 # 'world'
print(p.search("hello world"))           # 'world'
print(p.search(" hello world!"))         # None
print(p.search("hello world\n"))         # 'world'
print(p.search("hello world\n\n"))       # None
print(p.search("\nhello_world "))        # None
print(p.search("world hello world"))     # 'world'

# 정규식에 ^과 $를 같이 쓰는 경우
# 해당 문자열과 정확히 동일한 문자열만 매칭됨
# -> 문자열의 처음부터 끝까지 정확히 일치됨 (\n 한번 제외)
print('^$-----------')
p = re.compile("^hello world$")
print(p.match("hello world"))           # 'hello world'
print(p.match("pello world"))           # None
print(p.match("hello world!"))          # None
print(p.match("hello python world"))    # None
print(p.match("hello world\n"))         # 'hello world'

# p.fullmatch(): 문자열 전체가 정확히 일치해야 하는 경우,
print('p.fullmatch()-----------')
print(p.fullmatch("hello world"))         # 'hello world'
print(p.fullmatch("hello world\n"))       # None