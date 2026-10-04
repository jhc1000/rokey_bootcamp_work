# escape.py

# 이스케이프(escape) 코드 : 미리 정의해둔 문자 조합
# "\n" = newline = LF(line feed)
# "\t" = tab 
# "\b" = backspace (커서 위치를 한칸 뒤로 이동)
# \' = 작은 따옴표(') 표시  '안녕! 난 \'민\'이라고 해~'
# \" = 큰 따옴표(") 표시 
# \\ = \ 표시
# "\r" = CR(carrige return)     # 커버를 현재 줄 가장 앞으로 이동
# 그 외에도 form feed*("\f"), vertical tab("\v") 등등

# repr() : 객체를 개발자가 확인하기 좋은 문자열로 표현
print("hello\t world!\n")
print(repr("hello\t world!\n"))
print("hi", end="\b")
print("kenneth \"lim\"", end="")
print("\rthanks")

str1 = 'test\b'
str2 = 'test'
str3 = str1 + str2
print(str3)
print(repr(str3))   # 'test\x08test'
print(len(str3))


# 다양한 파일 처리 모드
# 'r' : read
# 'w' : write
# 'a' : append
# 'r+' : read + write => 파일을 읽고 쓰기(기 데이터 존재)
# 'w+' : write + read => 파일을 새로 만들거나 비우고 쓰고 읽기
# 'a+' : append + read 