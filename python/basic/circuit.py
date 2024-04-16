# 목 연산과 나머지 연산으로 행렬 표현.
matrix = [
    [3, 7, 9],
    [4, 2, 6],
    [8, 1, 5],
]

for i in range(9):
    print(matrix[i // 3][i % 3])
