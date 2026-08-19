N = int(input())
cond_1 =  N%2 == 1 and N%3 == 0
cond_2 =  N%2 == 0 and N%5 == 0
if cond_1 or cond_2:
    print("true")
else:
    print("false")