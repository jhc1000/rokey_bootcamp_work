# find_min1.py

su = [ 5, 4, 7, 10, 6]

def fmin(fu: list):
    min = fu[0]
    for i in range(1, len(fu), 1):
        if min > fu[i]:
            min = fu[i]
    return min

result = fmin(su)
print('min =', result)

print('----------')
