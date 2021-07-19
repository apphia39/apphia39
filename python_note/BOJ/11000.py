# BOJ에서는 시간초과

n = int(input())
course = []

for _ in range(n):
    s, t = map(int, input().split())
    course.append([s, t])

course = sorted(course, key = lambda course: (course[0], course[1]))

last = [0]
answer = 1

for s, t in course:
    flag = 0

    for i in last:
        if s<i:
            continue
        last.remove(i)
        flag = 1
        break
    
    if flag == 0:
        answer += 1
    last.append(t)

print(answer)
