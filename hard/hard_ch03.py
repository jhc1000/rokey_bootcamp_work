# hard_ch03.py

from dataclasses import dataclass

@dataclass
class SensorLog:
    temp: float        # 타입 있음
    unit = "℃"         # 타입 없음

print(SensorLog(78.2))

log = SensorLog(78.2)
print(log.unit)
# 결과는?
# print(SensorLog(78.2, 2)) 
# 결과는 어떻게 될까요?
# TypeError: SensorLog.__init__() takes 2 positional arguments but 3 were given

print('---------')

# from dataclasses import dataclass

# @dataclass
# class Bad:
#     status: str = "OK"
#     temp: float
# 결과는?
# TypeError: non-default argument 'temp' follows default argument


print('---------')

# @dataclass
# class Bad:
#     history: list = []
# 결과는?
# ValueError: mutable default <class 'list'> for field history is not allowed: use default_factory


from dataclasses import dataclass, field

@dataclass
class Good:
    history: list[float] = field(default_factory=list)   # 객체마다 새 리스트
    
print('---------')


from dataclasses import dataclass

@dataclass
class Machine:
    name: str
    kind: str
    year: int # 단순히 힌트 하지만 있어야 나중에 변수 넣어줄수있음

m = Machine("WELD-02", "용접기", 2021)

print(m)
print(m.name)
print(m.kind)
print(m.year)

m2 = Machine("WELD-02", "용접기", 2021)
print(m == m2)
# True

print('-----------')

from enum import Enum

class Status(Enum):
    OK = "OK"
    WARN = "WARN"
    DANGER = "DANGER"

print(Status.WARN.name)
print(Status.WARN.value)
# 결과는?
# WARN
# WARN
print(Status.WARN)
print(Status["WARN"])
print(Status("WARN"))

print('-----------')

class Level(Enum):
    LOW = 1
    HIGH = 2

print(Level.HIGH.name)   # HIGH  (멤버의 이름)
print(Level.HIGH.value)  # 2     (멤버에 배정한 값)

print(Level["HIGH"])   # Level.HIGH  (이름으로)
print(Level(2))        # Level.HIGH  (값으로)

print('-----------')

from enum import Enum

# TODO 1: Status Enum을 정의하세요 (OK, WARN, DANGER 세 가지)
class Status(Enum):
    OK = "OK"
    WARN = "WARN"
    DANGER = "DANGER"

def func(row):
    if float(row[2]) > 85 and float(row[3]) > 0.7:
        return row + [Status.DANGER]   # TODO 2: Status 멤버로 교체
    elif float(row[2]) > 85:
        return row + [Status.WARN]     # TODO 2: Status 멤버로 교체
    elif float(row[3]) > 0.7:
        return row + [Status.WARN]    # TODO 2: Status 멤버로 교체

def check_equipment(rows, equip):
    # result = []
    result = [func(row) for row in rows if row[1] == equip]
    '''for row in rows:
        if row[1] == equip:
            result = func()
    '''
    '''        
            if float(row[2]) > 85 and float(row[3]) > 0.7:
                result.append(row + ["DANGER"])   # TODO 2: Status 멤버로 교체
            elif float(row[2]) > 85:
                result.append(row + ["WARN"])     # TODO 2: Status 멤버로 교체
            elif float(row[3]) > 0.7:
                result.append(row + ["WARN"])     # TODO 2: Status 멤버로 교체
    '''
    return result
    
# Test용 rows 데이터 정의 [시간, 설비명, 온도, 진동]
rows = [
    ["2026-07-01 02:07", "WELD-01", "91.5", "0.31"],
    ["2026-07-01 02:08", "WELD-01", "88.0", "0.85"],
    ["2026-07-01 02:09", "WELD-02", "70.0", "0.20"]
]

# TODO 3: 실행해서 결과에 Status 멤버가 담기는지 확인하세요
anomalies = check_equipment(rows, "WELD-01")
print(anomalies[0])

print('-----------')

from dataclasses import dataclass
from typing import Optional  # (또는 최신 문법 str | None 사용 가능)


@dataclass
class SensorLog:
    time: str
    equip: str
    temp: float
    vib: float

def judge(log: SensorLog, threshold: float, equip: str | None) -> bool:
    return ((equip is None or log.equip == equip) and log.temp > threshold)

def filter_high_temp_logs(logs: list[SensorLog], threshold: float = 80.0, equip: Optional[str] = None) -> list[SensorLog]:
    return [log for log in logs if judge(log, threshold, equip)]

