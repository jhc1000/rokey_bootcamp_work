# generator2.py

# 제너레이터 비교 목적 예제
# 1. 리스트 사용
import time

def longtime_job():
    print("job start")  
    time.sleep(1)   # 시간 지연 함수 (1초)
    return "done"

list_job = [longtime_job() for i in range(5)]
print(list_job[0])

# job start
# job start
# job start
# job start
# job start
# done
# 리스트는 할당할때 함수가 다 실행되고 그 반환값을 저장
