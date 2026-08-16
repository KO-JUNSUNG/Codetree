dic = {"book":3000, "mask": 1000}
N = int(input())

ans = "no"
for item, value in sorted(dic.items(), key = lambda x: x[1], reverse = True):
    if N >= value:
        ans = item
        break
print(ans)