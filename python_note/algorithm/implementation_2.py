# 구현(2) 시각 - 완전탐색(brute force) 문제
# 정수 N이 입력되면 00시 00분 00초부터 N시 59분 59초까지의
# 모든 시각 중에서 3이 하나라도 포함되는 모든 경우의 수를 구하여라.

n = int(input())

answer = 0
for i in range(n+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i)+str(j)+str(k):
                answer += 1

print(answer)