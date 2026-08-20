arr = list(map(int, input().split()))
arr_1 = arr[1::2]
arr_2 = arr[2::3]
print(f'{sum(arr_1)} {sum(arr_2)/len(arr_2):.1f}')