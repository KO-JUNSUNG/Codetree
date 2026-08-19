A = int(input())
B,C,D,E = map(int, input().split())

def bl(condition:bool): 
    if condition == True:
        print(1)
    else:
        print(0)

bl(A>B)
bl(A>C)
bl(A>D)
bl(A>E)