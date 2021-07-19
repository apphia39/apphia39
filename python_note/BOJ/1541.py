s = input()

# 마이너스 부호~마이너스 부호까지 사이의 숫자는 전부 더한 뒤 -를 씌운다.
buho = []
num = []
cur = ""

for i in s:
    if i == '+' or i == '-':
        buho.append(i)
        num.append(int(cur))
        cur = ""
    else:
        cur += i
num.append(int(cur))
buho.append('.')

answer = num[0]
buho_idx = 0
num_idx = 1
tmp = 0

while True:
    if buho[buho_idx] == '.':
        break

    if buho[buho_idx] == '-':
        tmp = num[num_idx]
        num_idx += 1
        buho_idx += 1
        while buho[buho_idx] == '+':
            tmp += num[num_idx]
            num_idx += 1
            buho_idx += 1
        answer -= tmp
    elif buho[buho_idx] == '+':
        answer += num[num_idx]
        num_idx += 1
        buho_idx += 1

print(answer)