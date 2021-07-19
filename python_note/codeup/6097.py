h, w = map(int, input().split())
arr = [[0]*w for _ in range(h)]

n = int(input())
for _ in range(n):
    l, d, x, y = map(int, input().split())
    if d==0: #가로
        for j in range(y-1, y-1+l):
            arr[x-1][j] = 1
    else: 
        for j in range(x-1, x-1+l):
            arr[j][y-1] = 1

for i in range(h):
    for j in range(w):
        print(arr[i][j], end=" ")
    print()