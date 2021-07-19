# 내장함수 : 기본 입출력 / 정렬 (import 구문 필요 없음)
data = [1, 2, 3, 4, 5]
result = sum(data)
print(result)       #15
print(min(data))    #1
print(max(data))    #5

data = [1, 5, 3, 8, 9]
print(sorted(data))  #[1, 3, 5, 8, 9]
print(sorted(data, reverse=True)) #[9, 8, 5, 3, 1]

arr = [("홍길동", 35), ("이순신", 75), ("아무개", 42)]
print(sorted(arr, key=lambda x: x[1], reverse=True))



# itertools : 반복되는 형태의 데이터를 처리하기 위한 기능 (순열, 조합)
# -> 모든 경우의 수를 고려해야할 경우 많이 사용
from itertools import permutations, combinations, product, combinations_with_replacement

# 순열
data = ['A', 'B', 'C']
result = list(permutations(data, 3)) #data에서 3개를 골라 나열하는 모든 경우의 수
print(result)

# 조합
result = list(combinations(data, 2)) #data에서 2개를 뽑아 모든 조합 구하기
print(result)

# 중복순열
result = list(product(data, repeat=2)) #data에서 2개를 뽑는 모든 순열 나열(중복 허용)
print(result)

# 중복조합
result = list(combinations_with_replacement(data, 2)) #data에서 2개를 뽑는 모든 조합 나열(중복 허용)



# heapq : heap 자료구조 제공 (우선순위 큐)
# bisect : binary search 기능 제공


# collections : deque, counter 등의 자료구조 포함
from collections import Counter
counter = Counter(['red', 'blue', 'red', 'green', 'blue', 'blue'])
print(counter['blue'])  #3
print(counter['red'])   #2
print(dict(counter))    #사전 자료형으로 변환



# math : 팩토리얼, 제곱근, GCD, 삼각함수, pi 등을 포함
import math

# 최소공배수 LCM 구하기
def lcm(a, b):
    return a * b // math.gcd(a, b)

print(math.gcd(21, 14))  #21과 14의 최대공약수 (GCD)
print(lcm(21, 14))       #21과 14의 최소공배수 (LCM)