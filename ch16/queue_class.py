# queue_class.py

class Queue:
    # 1. 큐 리스트 생성 : 데이터 공간 초기화
    def __init__(self):
        self.queue = []
    # 2. enqueue 메서드 구현
    def enqueue(self, data):
        return self.queue.append(data)
    # 3. dequeue 메서드 구현
    def dequeue(self):
        # - 큐가 비어 있지 않은 경우
        if not self.is_empty():
            return self.queue.pop(0)
        return
    # 4. 큐 내 데이터 유무 확인 메서드 구현
    def is_empty(self):
        if len(self.queue) == 0:
            return True
        return False
    # 5. 큐 상태 반환 메서드
    def status_queue(self):
        return self.queue
    
if __name__ == "__main__":
    q1 = Queue()
    q1.dequeue()
    print(q1.status_queue())
    q1.enqueue(1)
    print(q1.status_queue())
    q1.enqueue(2)
    print(q1.status_queue())
    q1.enqueue(3)
    print(q1.status_queue())
    q1.dequeue()
    print(q1.status_queue())
    q1.dequeue()
    print(q1.status_queue())
    q1.dequeue()
    print(q1.status_queue())