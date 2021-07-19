d = [[0] * 19 for _ in range(19)]
for i in range(19):
    d[i] = list(map(int, input().split()))

n = int(input()) #뒤집기 횟수
for _ in range(n):
    x, y = map(int, input().split())
    value = d[x-1][y-1]
    
    for i in range(19):
        if d[x-1][i] == 0:
            d[x-1][i] = 1
        else:
            d[x-1][i] = 0
        if d[i][y-1] == 0:
            d[i][y-1] = 1
        else:
            d[i][y-1] = 0
    
    d[x-1][y-1] = value

for i in range(19):
    for j in range(19):
        print(d[i][j], end=" ")
    print()