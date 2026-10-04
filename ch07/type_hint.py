# type_hint.py

# def 함수명(매개1: 타입1, 매개2: 타입2) -> 반환타입:
#     코드블록
#     return 반환값

def add(x: int, y: int) -> int:
    return x + y
print(add(3, 5))
print(add(3.4, 23.2), type(add(3.4, 23.2)))
print(add("12","34"))
