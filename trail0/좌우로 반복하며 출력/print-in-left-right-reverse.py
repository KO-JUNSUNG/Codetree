N = int(input())

# 1부터 N까지 문자열로 미리 생성 (예: ['1', '2', '3', '4'])
forward = [str(i) for i in range(1, N + 1)]
backward = forward[::-1]  # 역순 슬라이싱 (예: ['4', '3', '2', '1'])

for i in range(N):
    if i % 2 == 0:
        print("".join(forward))
    else:
        print("".join(backward))