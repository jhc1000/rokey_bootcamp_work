# file_open.py

import os           # os 접근하는 라이브러리
print(os.getcwd())  # getcwd() 현재 작업중인 디렉토리(current working directory) 반환

# # 파일 객체 = open(경로, 모드)
# f = open(r"C:\rokey\py_work\ch12\file_open.py", "r") # 윈도우는 \ 도 사용가능 but r"" 사용
# # \n 이스케이프 코드
# f = open("C:/rokey/py_work/ch12/file_open.py", "w")
# f = open(r"ch12\file_open.py", "a")

# 파일 열기
# f = open("C:/rokey/py_work/ch12/file1.txt", "w")
f = open("ch12/file2.txt", "w")


# 파일 닫기
f.close()

# code 신호
