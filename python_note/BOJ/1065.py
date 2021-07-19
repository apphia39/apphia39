n = int(input())
l = [[] for _ in range(n+1)]
answer = 0

for i in range(1, n+1):
    num = i
    while num > 0:
        l[i].append(num%10)
        num //= 10
    l[i].reverse()

for i in range(1, n+1):
    flag = 0

    if len(l[i]) <= 2:
        answer += 1
    else:
        d = l[i][1]-l[i][0]
        for idx in range(len(l[i])-1):
            if l[i][idx+1]-l[i][idx] != d:
                flag = 1
                break
        if flag == 0:
            answer += 1

print(answer)
