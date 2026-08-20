middle_, end_ = map(int,input().split())

if middle_ >= 90:
    if end_ >= 95:
        print(100000)
    elif end_ >= 90:
        print(50000)
    else:
        print(0)
else:
    print(0)        

