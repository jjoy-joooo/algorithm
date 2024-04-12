# 단어 정렬
# import sys
# input = sys.stdin.readline

N = int(input())
words = set(input().rstrip() for _ in range(N))

answer = sorted(words, key=lambda x: (len(x), x))

for i in answer:
    print(i)
