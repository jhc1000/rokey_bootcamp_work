# try_except.py

# try:
#     코드블록
# except 예외클래스:
#     코드블록
# finally:
#     코드블록
    
# while True:
#     x = int(input("Please enter a number: "))  # ValueError
#     break

# try 이후로 에러가 뜨든 안뜨든 finally 문을 들어감.
while True:
    try:
        print("명령어1")
        x = int(input("Please enter a number: "))   # ValueError
        print(x + '2')                              # TypeError
        print("명령어2")
        break
    except ValueError as e:
        print("Oops! That was no valid number. Try again...")
        print("에러 관련 정보: ", e)
    except TypeError:
            print("TypeError 발생! 데이터 타입 확인 요망.")
    except (ValueError, TypeError):
        print("Oops! That was no valid number. Try again...")
    except Exception as e:
        print(e)    
    finally:
        print("finally 동작")
print("프로그램 완료!")

