# 문제풀이_2 : 미로찾기
# NxM 크기의 미로에 갇혀있다. 1인 부분을 따라 탈출하도록 한다.
# 시작 위치는 1, 1이며, 미로의 출구는 N,M이다. 
# 반드시 한 칸씩 이동한다.
# 탈출하기 위해 움직이는 최소 칸의 개수는? 

# BFS로 해결하기
# 시작지점에서 가까운 노드부터 모든 노드를 탐색
# 상, 하, 좌, 우를 탐색하며 모든 노드의 최단 거리 값을 기록한다.

from collections import deque

n, m = map(int, input().split())
graph = []
# 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(n):
    graph.append(list(map(int, input())))

def bfs(x, y):
    queue = deque()
    queue.append((x,y))

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if nx<0 or nx>=n or ny<0 or ny>=m:
                continue #범위 벗어나면 무시

            if graph[nx][ny] == 0:
                continue #0인 경우 무시

            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))

    return graph[n-1][m-1]

print(bfs(0, 0))
