def boolean_(condition):
    if condition == True:
        print(1)
    else:
        print(0)
A,B = map(int,input().split())

boolean_(A>=B)
boolean_(A>B)
boolean_(B>=A)
boolean_(B>A)
boolean_(A==B)
boolean_(A!=B)
