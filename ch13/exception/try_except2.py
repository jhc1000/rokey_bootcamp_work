# try_except2.py

print("try_except2")
path = r"ch13\exception\myfile.txt"
# 모드 기본값 'r'
# f = open(path)
# s = f.readline()
# i = int(s.strip())

# try:
#     코드블록
# except 예외클래스:
#     코드블록
    
try:
    # f = open(path, 'w')
    # f.write("Hello")
    # f.write("123")
    f = open(path) # FileNoFoundError
    s = f.readline()    
    i = int(s.strip())  # ValueError -> "H"
    print(i)
except FileNotFoundError:
    print("파일을 찾을 수 없습니다.")
except OSError as err:
    print("OsError: ", err)
except ValueError as e:
    print("정수형으로 변환 할수 없습니다.")
    print("발생 에러 정보:", e)
except Exception as e:
    print("예측 되지 않은 발생 에러 정보:", e)
# except 순서를 잘 봐야한다.
finally:
    f.close()       # 만약, 에러로 인해 건너뛰는 경우 처리
print("program exit")

# finally 사용 이유
# 예외 발생 여부와 관계없이 반드시 실행해야하는 코드 작성
# 예) 파일 닫기, 데이터베이스 연결 종료, 프로그램 종료 전 정리 작업