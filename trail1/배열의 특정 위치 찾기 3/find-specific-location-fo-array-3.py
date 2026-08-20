arr = list(map(int,input().split()))
end_ = 0
for i in range(len(arr)):
    if arr[i] == 0:
        end_ = i
        break

print(sum(arr[end_-3:end_]))
