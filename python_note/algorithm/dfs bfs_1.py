# DFS, BFS 배우기 전 "튜토리얼"

# 그래프 탐색 알고리즘 - DFS, BFS
# <알아야 할 자료구조>
# 1. 스택 자료구조(LIFO) - 리스트 삽입(append) / 삭제(pop)
# 2. 큐 자료구조(FIFO) - list사용해도 되지만 시간복잡도 면에서 비효율적이므로 deque 라이브러리 사용하자!
#    from collection import deque
#    queue = deque()
#    queue.append(i) //맨 뒤에 삽입
#    queue.popleft() //가장 앞에 있는 애를 pop
#    queue.reverse() //리버스

# 재귀함수(recursive function) - 자기 자신을 다시 호출하는 함수
#  - 반드시 종료조건을 명시해주어야 한다. 그렇지 않으면 무한히 호출된다.
#  - factorial 구현 예제
def factorial_recursive(i):
    if i <= 1:
        return 1
    return i*factorial_recursive(i-1)
    
print("팩토리얼 n:", end=" ")
n = int(input())
print(f"result is {factorial_recursive(n)}")

#  - 최대공약수 계산(유클리드 호제법) 예제
#    : R = 큰수%작은수. 큰수와 작은수의 최대공약수는 작은수와 R의 최대공약수와 같다.
def gcd(a, b):
    if a%b == 0:
        return b
    return gcd(b, a%b)

print("두 수:", end=" ")
a, b = map(int, input().split())
print(f"result is: {gcd(a, b)}")

