n = int(input())

member = []

for i in range(1, n+1):
    age, name = input().split()
    age = int(age)

    member.append([i, age, name])

member = sorted(member, key=lambda member:(member[1], member[0]))

for num, age, name in member:
    print(age, name)