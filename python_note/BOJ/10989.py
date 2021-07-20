import sys

n = int(input())
count_list = [0]*10001

for _ in range(n):
    num = int(sys.stdin.readline())
    count_list[num] += 1

for i in range(10001):
    for j in range(count_list[i]):
        print(i)