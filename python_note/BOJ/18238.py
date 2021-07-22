s = list(input())

start = 'A'
answer = 0

for alpha in s:
    diff = abs(ord(alpha)-ord(start))
    if diff > 13:
        answer += 26-diff
    else:
        answer += diff
    start = alpha

print(answer)