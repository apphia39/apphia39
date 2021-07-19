n = int(input())
p = list(map(int, input().split()))

answer = 0
start = 0
num = 0
for i in p:
    if i < start:
        num += 1
    elif i > start:
        answer = max(num, answer)
        start = i
        num = 0

answer = max(num, answer)
print(answer)

