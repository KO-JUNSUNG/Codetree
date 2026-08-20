a_age, a_sex = input().split()
a_age = int(a_age)
b_age, b_sex = input().split()
b_age = int(b_age)
if (a_sex == "M" and a_age >= 19) or (b_sex == "M" and b_age >= 19):
    print(1)
else:
    print(0)