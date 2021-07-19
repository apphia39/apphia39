# greedy(2) 1이 될 때까지
# n이 1이 될 때까지 두 과정 중 하나를 반복적으로 선택하여 수행
# (1) n에서 1을 뺀다
# (2) n을 k로 나눈다. 단, n이 k로 나누어 떨어지는 경우에만 선택 가능하다.
# 정당성 분석 : n이 아무리 큰 수여도, k로 나눈다면 기하급수적으로 빠르게 줄일 수 있다.

# 조건 : n>=1, k>=2
n, k = map(int, input().split())
answer = 0

while n>1:
    if n%k == 0:
        n //= k
    else:
        n -= 1
    answer += 1

print(answer)        