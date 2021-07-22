n = int(input())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

visited = [False]*len(a)

a.sort()
answer = 0

for i in a:
    idx = b.index(max(b))
    answer += i * b[idx]
    b[idx] = -1

print(answer)