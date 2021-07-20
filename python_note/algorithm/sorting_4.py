# O(N+K), N=데이터 개수, K=데이터 중 최댓값
# 4. 계수 정렬(count 정렬) 
# 특정 조건이 부합하는 경우에만 사용 가능함
# 데이터 크기 범위가 제한되어 정수 형태로 표현할 수 있을 때 사용 가능
# 매우 빠르게 동작

array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]
count = [0] * (max(array)+1)

for i in array:
    count[i] += 1

for i in range(0, max(array)+1):
    for j in range(count[i]):
        print(i, end=" ")