# generator2-1.py

# 제너레이터 비교 목적 예제
# 1. 리스트 사용
import time

def longtime_job():
    print("job start")  
    time.sleep(1)   # 시간 지연 함수 (1초)
    return "done"

# list_job = [longtime_job() for i in range(5)]
# print(list_job[0])

# job start
# job start
# job start
# job start
# job start
# done
# 리스트는 할당할때 함수가 다 실행되고 그 반환값을 저장


# 2. 제너레이터 컴프리헨션 사용

gen_job = (longtime_job() for i in range(5))
print(next(gen_job))
# print(next(gen_job))
# print(next(gen_job))
# print(next(gen_job))
# print(next(gen_job))
# for i in gen_job:
#     print(i)
# job start
# done
# 제너레이터는 객체로 저장해놓고 next 실행 될 때 함수가 실행
print("__iter__" in dir(gen_job))  # True  
print("__next__" in dir(gen_job))  # True

## 차이점:
# 1. 실행 "타이밍" 다름 : 리스트는 한꺼번에, 제너레이터는 호출될때
# 2. 중간에 정지 가능 : 제너레이터는 정지 가능
# 3. 메모리 사용량 : 제너레이터가 더 적게 씀