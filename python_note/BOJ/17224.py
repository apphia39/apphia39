n, l, k = map(int, input().split())
score = 0
sub_list = []

for _ in range(n):
    sub1, sub2 = map(int, input().split())
    sub_list.append([sub1, sub2])

sub_list = sorted(sub_list, key=lambda sub_list:sub_list[1])

for sub1, sub2 in sub_list:
    if k == 0:
        break

    if sub2 <= l:
        score += 140
        k -= 1
    elif sub1 <= l and sub2 > l:
        score += 100
        k -= 1

print(score)