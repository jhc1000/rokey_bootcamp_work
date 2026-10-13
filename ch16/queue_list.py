# queue_list.py

# 큐 구현 : 리스트 활용

# 빈 큐 구현
queue = []

# Enqueue 연산 구현
queue.append(1)
print(f"queue = {queue}")
queue.append(2)
print(f"queue = {queue}")
queue.append(3)
print(f"queue = {queue}")
queue.append(4)
print(f"queue = {queue}")

# Dequeue 연산 구현
queue.pop(0)
print(f"queue = {queue}")
queue.pop(0)
print(f"queue = {queue}")
queue.pop(0)
print(f"queue = {queue}")
queue.pop(0)
print(f"queue = {queue}")

# 큐가 비어 있는 경우
if queue == []:
    print("is empty!")
else:
    queue.pop(0)
    print(f"queue = {queue}")
