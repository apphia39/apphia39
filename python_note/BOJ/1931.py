n = int(input())
meetings = []

for _ in range(n):
    x, y = map(int, input().split())
    meetings.append([x, y])

meetings = sorted(meetings, key = lambda key:(key[1], key[0]))
# 끝나는 시간이 제일 빠른 애 중에서 시작 시간이 제일 빠른 애
end = 0
answer = 0
for x, y in meetings:
    if x>=end:
        answer += 1
        end = y

print(answer)

