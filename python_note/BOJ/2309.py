from itertools import combinations

answer = []

for _ in range(9):
    answer.append(int(input()))

result = list(combinations(answer, 7))
answer.clear()

for l in result:
    if sum(l) == 100:
        for i in l:
            answer.append(i)
        answer.sort()
        for i in answer:
            print(i)
        break