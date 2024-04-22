N = int(input())

for _ in range(N):
    text = input()
    total = 0
    tmp = 0

    for i in text:
        if i == "O":
            tmp += 1
            total += tmp
        else:
            tmp = 0

    print(total)
