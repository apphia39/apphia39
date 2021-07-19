n = int(input())
seat_str = input()
seat_list = ["*"]

i = 0

while True:
    if i == n:
        break
    if seat_str[i] == 'S':
        if seat_list[-1] != '*':
            seat_list.append("*")
        seat_list.append("S")
        seat_list.append("*")
        i += 1
    else:
        if seat_list[-1] != '*':
            seat_list.append("*")
        seat_list.append("L")
        seat_list.append("L")
        seat_list.append("*")
        i += 2

answer = min(seat_list.count("*"), n)
print(answer)
