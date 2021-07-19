from collections import deque

n = int(input())
graph = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
answer = []
total = 0

for _ in range(n):
    graph.append(list(map(int, input())))

def bfs(start_x, start_y):
    queue = deque()
    queue.append((start_x, start_y))
    num = 0

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if nx<0 or ny<0 or nx>=n or ny>=n:
                continue
            if graph[nx][ny] == 0:
                continue
            num += 1
            graph[nx][ny]=0
            queue.append((nx, ny))

    if num == 0:
        return 1
    return num
        
for x in range(n):
    for y in range(n):
        if graph[x][y] == 1:
           answer.append(bfs(x, y))
           total += 1

answer.sort()

print(total)
for i in answer:
    print(i)
