a, m, d, n = map(int, input().split())

for _ in range(2, n+1):
    a = a*m+d

print(a)