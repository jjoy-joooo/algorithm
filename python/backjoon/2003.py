# 수열의 합 2
N, M = list(map(int, input().split()))
arr = list(map(int, input().split()))

L = 0
R = 0
CNT = 0

while R < N:
    SUM = sum(arr[L : R + 1])

    if SUM == M:
        CNT += 1
        R += 1
    elif SUM > M:
        L += 1
    else:
        R += 1


print(CNT)
