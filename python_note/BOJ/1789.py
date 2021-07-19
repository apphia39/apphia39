s = int(input())

num = 0 #지금까지 더한 수
answer = 0 #자연수 개수
i = 1

while True:
    num += i
    answer += 1
    i += 1
    if num == s:
        print(answer)
        break
    elif num > s: # ex) 1+2+3+...+19+20 = 200 > 210이므로 1+2+3+...+19에서 마지막 19를 29로 바꿔주는 식으로!
        print(answer-1)
        break