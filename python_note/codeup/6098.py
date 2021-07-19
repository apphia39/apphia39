d = [[0]*10 for _ in range(10)]

for i in range(10):
    d[i] = list(map(int, input().split()))

x = 1
y = 1
while 1:
    #맨 아래 가장 오른쪽에 도착한 경우
    if y == 8 and x == 8: 
        d[x][y] = 9
        break
    #먹이를 찾은 경우
    if d[x][y] == 2:
        d[x][y] = 9
        break
    #움직일 수 없는 경우
    if d[x+1][y] == 1 and d[x][y+1] == 1:
        d[x][y] = 9
        break
    
    d[x][y] = 9
    #오른쪽에 길이 없는 경우
    if d[x][y+1] == 1:
        x += 1
    else:
        y += 1

for i in range(10):
    for j in range(10):
        print(d[i][j], end=" ")
    print()