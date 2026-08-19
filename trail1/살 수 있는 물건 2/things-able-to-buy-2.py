dic = {"book": 3000, "mask": 1000, "pen": 500}
N = int(input())
ans = "no"
for item, price in dic.items():
    if N >= price:
        ans = item
        break
print(ans)