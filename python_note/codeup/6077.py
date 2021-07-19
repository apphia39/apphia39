n = int(input())

answer=0

for i in range(n+1):
    if i%2 == 0:
        answer+=i

print(answer)    