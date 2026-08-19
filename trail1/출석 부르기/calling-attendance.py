dic = {1:"John", 2: "Tom", 3:"Paul"}
student = int(input())
if student not in dic:
    print("Vacancy")
else:
    print(dic[student])