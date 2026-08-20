scores = list(map(int,input().split()))
for idx, item in enumerate(scores):
    if item == 0:
        scores = scores[:idx]
        break

ans = []
for i in scores:
    if i%2 == 0:
        ans.append(i)
print(len(ans), sum(ans))