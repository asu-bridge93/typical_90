H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]

col_sum = [0] * (W + 1)
row_sum = [0] * (H + 1)

for i in range(H):
    for j in range(W):
        col_sum[j] += A[i][j]
        row_sum[i] += A[i][j]

for i in range(H):
    for j in range(W):
        print(col_sum[j] + row_sum[i] - A[i][j], end=" ")
    print()
