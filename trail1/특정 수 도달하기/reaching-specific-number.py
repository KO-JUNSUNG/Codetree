arr = list(map(int, input().split()))
cnt = False
i = 0
for idx, element in enumerate(arr):
    if element >= 250:
        cnt = True
        i = idx
        break
if cnt == True:
    arr = arr[0:i]
# print(len(arr))
print(f'{sum(arr)} {sum(arr)/len(arr):.1f}')