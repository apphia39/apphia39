n = int(input())

answer = 0

while n > 0:
    if n%5 == 0:
        break
    answer += 1
    n -= 3

if n < 0:
    print("-1")
elif n%5 == 0:
    answer += n//5
    print(answer)
else:
    print(answer)