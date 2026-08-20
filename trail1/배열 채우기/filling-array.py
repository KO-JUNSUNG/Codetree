scores = list(map(int,input().split()))

for idx, score in enumerate(scores):
    if score == 0:
        end_ = idx
        scores = scores[0:idx]
        break
print(*scores[::-1])