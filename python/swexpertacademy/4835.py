# 구간합
for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    # 배열 순회
    i, j = 0, M - 1
    min_sum = sum(arr[: M + 1])
    max_sum = min_sum
    cur_sum = min_sum
    i += 1
    j += 1

    while j < N:
        cur_sum = cur_sum - arr[i - 1] + arr[j]
        max_sum = max(cur_sum, max_sum)
        min_sum = min(cur_sum, min_sum)
        i += 1
        j += 1

    print(f"#{tc} {max_sum - min_sum}")
