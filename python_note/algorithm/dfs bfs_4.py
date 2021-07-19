# 문제풀이_1 : 음료수 얼려 먹기
# NxM 크기의 얼음틀이 있다. 구멍이 뚫린 부분은 0, 칸막이 부분은 1이다.
# 구멍이 뚫려있는 부분끼리 상, 하, 좌, 우로 붙어있는 경우 서로 연결된 것으로 간주한다.
# 얼음 틀의 모양이 주어질 때 생성되는 총 아이스크림의 개수는?

# DFS로 푸는 경우
# 특정 지점의 상, 하, 좌, 우를 살펴 값이 0이면서 아직 방문하지 않은 지점이 있다면 방문
# 방문한 지점에서 다시 상, 하, 좌, 우를 살피면서 방문을 진행하는 과정을 반복하면 연결된 모든 지점을 방문 가능
# 모든 노드에 대해 위 과정을 반복하며 방문하지 않은 지점의 수를 카운트

n, m = map(int, input().split())
graph = []
answer = 0

# 입력
for i in range(n):
    graph.append(list(input()))

def dfs(x, y):
    if x<0 or y<0 or x>=n or y>=m:
        return False #범위 벗어나는 경우
    
    if graph[x][y] == "0": #현재 노드를 아직 방문 안한 경우
        graph[x][y] = "1" #방문처리
        dfs(x-1, y) #상
        dfs(x+1, y) #하
        dfs(x, y-1) #좌
        dfs(x, y+1) #우
        return True

    return False

for x in range(n):
    for y in range(m):
        if dfs(x, y) == True: # 현재 위치에서 dfs 수행
            answer += 1

print(answer)