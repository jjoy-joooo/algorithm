# 2711 - 오타맨 고창영
T = int(input())

for i in range(T):
    num, text = input().split()
    num = int(num)

    result = text[: num - 1] + text[num:]
    print(result)

for _ in range(T):
    idx, word = map(int, input().split())
    idx = int(idx) - 1
    word = list(word)
    word.pop(idx)
    ans = "".join(word)
    print(ans)
