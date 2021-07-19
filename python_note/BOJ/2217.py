n = int(input())
w = []

for _ in range(n):
    weight = int(input())
    w.append(weight)

w.sort()
answer = max(w)

for i in w:
    if(i*n > answer):
        answer = i*n
    n -= 1

print(answer)