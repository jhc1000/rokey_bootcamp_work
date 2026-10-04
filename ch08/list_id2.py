# list_id2.py

def fk(cb):
    total = 0
    for sb in range(0, 3, 1):
        total=total+cb[sb]
    cb[2]=total
    return cb

ca=[10, 20, 30]
print('ca:', ca)
cd = fk(ca)
print('ca:', ca)
print('cd:', cd)
