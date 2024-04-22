"""
문제 풀이(for문으로 풀어야 한다.)
1. 같은 숫자가 발생 x.
2. 증가하는 수이어야 한다.
3. 작아진후 커지면, 증가해야 한다.
4. 오르막길 없으면 0으로 표현되어야 한다.
---
1) 작거나 최초 값을 할당해야 한다.
"""

N = int(input())
arr = list(map(int, input().split()))
tmpArr = []
sumArr = []
flag = False

for i in arr:
    tmpArr.append(i)

    if tmpArr[len(tmpArr) - 1]:
        print()
    # if len(tmpArr) >= 1 and tmpArr[len(tmpArr) - 1] > i:
    #     tmpArr[]

    # if len(tmpArr) == 0 or tmpArr[len(tmpArr) - 1] <= i:

    #     if tmpArr[len(tmpArr) - 1] == i:
    #         flag = True

    # print()
