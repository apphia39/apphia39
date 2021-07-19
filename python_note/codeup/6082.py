n = int(input())
count = 0

for i in range(1, n+1):
    num = i
    while i >= 1:
        if i%10==3 or i%10==6 or i%10 == 9:
            count += 1
        i = i//10
    if count > 0:
        print("X", end=" ")
        count = 0
    else:
        print(num, end=" ")
        