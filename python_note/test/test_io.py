# input() : 한 줄의 문자열을 입력받는다.
# map() : 리스트의 모든 원소에 각각 특정 함수를 적용할 때 사용
#         ex) list(map(int, input().split()))
#         ex) a, b, c = map(int, input().split()) : 입력받는 데이터가 3개로 정해진 경우


# 첫 줄에 데이터 개수 입력
n = int(input())
# 각 데이터를 공백 기준으로 구분하여 입력
data = list(map(int, input().split()))
# 내림차순으로 정렬
data.sort(reverse=True)
# 출력
print(data)


# 사용자로부터 입력을 최대한 빠르게 받아야 하는 경우
# sys.stdin.readline() 메서드 사용
# 단, 입력 후 엔터가 줄 바꿈 기호로 입력되므로 rstrip() 메서드를 함께 사용
import sys
data = sys.stdin.readline().rstrip()
print(data)


# 출력
# 기본적으로 print() 이후에는 줄바꿈
print(7, end=" ") # 줄바꿈 안하기
print(8) # 줄바꿈 자동으로 됨

# 정수형을 문자열과 같이 출력하는 경우
answer = 9
print("정답은 "+ str(answer) + "입니다")


# 정수형을 문자열과 같이 출력하는 경우 : f-string
answer = 9
print(f"정답은 {answer}입니다.")
