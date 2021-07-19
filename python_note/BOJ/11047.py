n, k = map(int, input().split())

a = []
answer = 0

# 한 줄씩 오름차순으로 가치 입력받기
for _ in range(n):
    tmp = int(input())
    a.append(tmp)

# 가치 큰 돈이 앞에 오도록 reverse
a.sort(reverse=True)

for i in a:
    answer += k//i
    k %= i

print(answer)