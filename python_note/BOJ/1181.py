n = int(input())
str = []

for _ in range(n):
    s = input()
    if s not in str:
        str.append(s)


str = sorted(str, key=lambda str:(len(str), str))

for i in str:
    print(i)