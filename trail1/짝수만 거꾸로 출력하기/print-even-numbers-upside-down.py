N = int(input())
scores = list(map(int,input().split()))
ans = []
for score in scores:
    if score%2 == 0:
        ans.append(score)
print(*ans[::-1])
