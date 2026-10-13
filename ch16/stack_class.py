# stack_class.py

class Stack:
    # 1. 스택 리스트 생성
    def __init__(self):
        self.stack=[]
    # 2. push 메서드 구현
    def push(self, data):
        self.stack.append(data)
    # 3. pop 메서드 구현
    def pop(self):
        # - 스택이 비어 있지 않은 경우
        if not self.is_empty():
            return self.stack.pop()
        return
    # 4. 스택 내 데이터 유무 확인 메서드 구현
    def is_empty(self):
        if len(self.stack) == 0:
            return True
        return False
    # 5. 스택 최상위 데이터 확인 메서드 구현
    def peak(self):
        # - 스택이 비어 있지 않은 경우
        if not self.is_empty():
            return self.stack[-1]
        return
    # 6. 스택 상태 반환 메서드
    def status_stack(self):
        return self.stack

if __name__ == "__main__":
    s1 = Stack()
    print(s1.peak())
    s1.pop()
    s1.push(1)
    print(s1.status_stack())
    s1.push(2)
    print(s1.status_stack())
    s1.pop()
    print(s1.status_stack())
    s1.push(3)
    print(s1.status_stack())
    s1.push(4)
    print(s1.peak())
    print(s1.status_stack())