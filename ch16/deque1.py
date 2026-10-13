# deque1.py

from collections import deque

dq = deque()

dq.append(1)
print(dq)

dq.appendleft(2)
print(dq)

dq.pop()
print(dq)

dq.popleft()
print(dq)

if not dq:
    print("empty")
else:
    dq.popleft()
    print(dq)

# 초기값 설정
dq2 = deque([1,2,3,4])

# 우측회전(1) 
dq2.rotate(1)
print(dq2) # deque([4, 1, 2, 3])

# 좌측회전(-1)
dq2.rotate(-1)
print(dq2) # deque([1, 2, 3, 4])

dq2.rotate(-2)
print(dq2) # deque([3, 4, 1, 2])

# 리스트로 변환
print(list(dq2))
