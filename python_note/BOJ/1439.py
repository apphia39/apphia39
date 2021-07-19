s = list(map(int, input()))
zero_num = 0
one_num = 0
prev = -1

for i in s:
    if prev != i:
        if i==0: zero_num += 1
        else: one_num += 1
    prev = i

print(min(zero_num, one_num))