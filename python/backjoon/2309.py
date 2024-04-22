# 일곱 난쟁이
arr = [int(input()) for _ in range(9)]
len_arr = len(arr)
SUM = sum(arr)

arr.sort()

flag = False
for i in range(len_arr):
    for j in range(i, len_arr):

        tmp = SUM - arr[i] - arr[j]
        if tmp == 100:
            arr.remove(arr[i])
            arr.remove(arr[j])
            if flag == False:
                flag = True
            if flag:
                break
    if flag:
        break

for i in arr:
    print(i)
