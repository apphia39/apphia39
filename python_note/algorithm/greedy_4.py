# greedy(4) 모험가 길드
# 모험가 길드에서는 n명의 모험가를 대상으로 '공포도'를 측정
# '공포도'가 x인 모험가는 반드시 x명 이상으로 구성한 모험가 그룹에 참여해야 여행을 떠날 수 있도록 규정
# 최대 몇 개의 모험가 그룹이 만들어질 수 있는가?

n = int(input())
list_a = list(map(int, input().split()))

list_a.sort()
people = 0  # 현재 그룹에 포함된 모함가 수
answer = 0 # 총 그룹 수

for i in list_a: # 공포도 낮은 것부터 하나씩 확인
    people += 1  # 현재 그룹에 해당 모험가를 포함시키기
    if people >= i: # 현재 그룹에 포함된 모험가 수가 현재 공포도보다 크거나 같으면, 그룹 결성
        answer += 1 # 총 그룹 수 증가시키기
        people = 0 # 현재 그룹에 포함된 모험가 수 초기화

print(answer)
