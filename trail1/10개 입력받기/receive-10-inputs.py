scores = list(map(int,input().split()))
for idx, item in enumerate(scores):
    if item == 0:
        scores = scores[0:idx]
        break
print(f'{sum(scores)} {sum(scores)/len(scores):.1f}')