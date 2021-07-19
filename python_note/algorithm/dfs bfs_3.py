# BFS
# : 너비 우선 탐색(가까운 노드부터 우선적으로 탐색)
# : 큐 자료구조 사용
# 1) 탐색 시작노드를 큐에 삽입하고 방문처리
# 2) 큐에서 노드를 꺼낸 뒤, 해당 노드의 인접 노드 중 방문하지 않은 노드를 모두 큐에 삽입하고 방문처리
# 3) 더이상 2번 과정을 수행할 수 없을 때까지 반복
# 각 간선의 비용이 같을 때 최단거리 계산할 경우 많이 사용

# BFS 예제 : 1 2 3 8 7 4 5 6
from collections import deque
graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]
visited = [False]*9

def bfs(graph, start, visited):
    queue = deque([start]) #시작 노드를 큐에 넣는다
    visited[start] = True #시작 노드를 방문처리한다

    while queue: #큐가 빌 때까지 반복
        v = queue.popleft() #제일 앞에 있는 애 pop
        print(v, end=" ")
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

bfs(graph, 1, visited)