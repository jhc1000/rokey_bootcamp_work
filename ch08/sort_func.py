# sort_func.py
# 정렬 함수

# 1. list.sort() 
# - 특징 : 원본 리스트 자체를 정렬
nums = [30, 10, 50, 20, 40]
nums.sort()
print(nums)

# [10, 20, 30, 40, 50]

print('----------')

# 2. sorted() 내장함수
nums = [30, 10, 50, 20, 40]
nums_new = sorted(nums)
print(nums)
print(nums_new)

print('----------')