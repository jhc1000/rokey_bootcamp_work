# slash.py

# 역슬래시 문제
import re

# p = re.compile("\section")  # None
# p = re.compile("\\section")   # None
# p = re.compile("\\\\section")  # \\section
p = re.compile(r"\\section")   # \\section
# m = p.match(r"\section python hello thanks")
m = p.match(r"\section python hello thanks")
print(m)

# 1. 파이썬 리터헐 규칙(이스케이프)
# # "\\" -> "\"
# # "\\\\" -> "\\"

# 2. '\s' 정규표현식 화이트스페이스 의미 
# "\\section" -> "\section"

# 정규식 메타문자 -> \s, \d, \w
# 이스케이프 문자 ->  \n, \t, \r, \f, \v
