timer = [300, 60, 10]

t = int(input())
answer = []

for i in timer:
    answer.append(t//i)
    t %= i

if t > 0:
    print("-1")
else:
    for i in answer:
        print(i, end=" ")
