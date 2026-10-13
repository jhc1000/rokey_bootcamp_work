# re1.py

# 패턴객체 = re.compile(메타문자를 활용한 정규표현식)
# 매치객체 = 패턴객체.match(패턴과 일치 여부를 확인할 문자열)

# 축약형태
# 매치객체 = re.match("정규표현식", "검색대상문자열")

import re

# p = re.compile("[a-z]+")
# m = p.match("python")   # 'python'

m = re.match("[a-z]+", "python")  # 'python'
# m = re.match("[a-z]+", "3 python")  # 'python'
print(m)

m = re.search("[a-z]+", "python")  # 'python'
# m = re.match("[a-z]+", "3 python")  # 'python'
print(m)

# 패턴객체를 여러번 사용할시 compile() 하고 쓰는게 편함
print('---------')
