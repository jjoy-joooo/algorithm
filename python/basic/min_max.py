nums = [7, 1, 4, 2, 5, 9]

print(min(nums), max(nums))

# 최댓값
max_num = nums[0]
for num in nums:
    if max_num < num:
        max_num = num
print("최댓값: ", max_num)

# 최솟값
min_num = nums[0]
for num in nums:
    if max_num > num:
        max_num = num
print("최솟값: ", max_num)
