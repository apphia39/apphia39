n = int(input())
l = list(map(int, input().split()))

l.sort()
k = 0
answer = 0

for i in l:
    k += i
    answer += k
    
print(answer)