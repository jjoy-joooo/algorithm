T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    nums = list(map(int, input().split()))
    answer = max(nums) - min(nums)
    print(f"#{tc} {answer}")
