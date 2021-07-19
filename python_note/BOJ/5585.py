money = int(input())
left = [500, 100, 50, 10, 5, 1]
money = 1000 - money
answer = 0

for i in left:
   answer += money//i
   money %= i

print(answer)