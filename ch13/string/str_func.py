# str_func.py

# 함수 사용시 확인 할 내용
# 1. 기능/동작
# 2. 매개변수 
# 3. 반환값

# 1. split()
# "문자열".split(구분자)
# 1. 기능/동작 : 구분자 기분 분리
# 2. 매개변수 : [구분자:str] = " " 
# 3. 반환값 : 구분된 문자열 -> list

my_string="Python is a popular programming language"
split_list=my_string.split()
print(split_list)

phone_num="010-5916-1554"
split_list=phone_num.split("-")
print(split_list)

print('--------')

# 2. strip()
# "문자열".strip()
# 1. 기능/동작 : 문자열 양 끝에 있는 공백(띄어쓰기, 탭, 개행문자 등)을 제거
# 2. 매개변수 : [제거할문자](생략시 공백)
# 3. 반환값 : 수정된 문자열 -> str

my_string="\t     Python is awesome!      \n"
stripped_string=my_string.strip()
print(stripped_string)
# 웹사이트 회원가입시 아이디 공백처리

print('--------')

# 3. join()
# 구분자.join(리스트)
# 1. 기능/동작 : iterable의 요소들를 구분자로 하나의 문자열로 결합
# 2. 매개변수 : iterable(문자열 요소 집합)
# 3. 반환값 : 연결된 문자열 -> str

my_list=["apple","banana","cherry"]
# my_list=["apple",123,"cherry"]      # TypeError 문자열들만 결합해
# joined_string=".".join(my_list)
joined_string=":".join(my_list)
# joined_string="/".join(my_list)
print(joined_string)

# 파일 경로 처리에 주로 사용

print('--------')
