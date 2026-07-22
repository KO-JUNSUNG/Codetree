N = int(input())
# 짝수 열일 때, 행수가 늘면 증가
# 홀수 열일 때, 행수가 늘면 감소
arr = [[1] * N for _ in range(N)]

for i in range(N):
    for j in range(N):
        if i % 2 == 0:
            arr[j][i] = j + 1 
        else:
            arr[j][i] = N - j

for i in range(N):
    for j in range(N):
        print(arr[i][j], end = "")
    print()
