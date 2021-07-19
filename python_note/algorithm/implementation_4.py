# 구현(4) 문자열 재정렬
# 알파벳 대문자와 숫자(0~9)로만 구성된 문자열이 입력으로 주어진다
# 모든 알파벳을 오름차순으로 정렬하여 이어서 출력한 뒤에,
# 그 뒤로 모든 숫자를 더한 값을 이어서 출력한다.

data = input()
str_alpha = []
num = 0

for i in data:
    if i.isalpha():
         str_alpha.append(i)
    else:
         num += int(i)

str_alpha.sort()
for i in str_alpha:
    print(i, end="")
print(num)