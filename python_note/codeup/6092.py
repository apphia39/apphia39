n = int(input())
list = list(map(int, input().split()))

for i in range(24):
    print(list.count(i), end=" ")