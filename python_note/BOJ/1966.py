from collections import deque

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    queue = deque(map(int, input().split()))
    turn = 0

    while queue:
        max_val = max(queue)
        answer = queue.popleft()

        if answer < max_val:
            m -= 1
            queue.append(answer)
            if m<0:
                m = len(queue) - 1
        else:
            m -= 1
            turn += 1
            if m==-1:
                print(turn)
                break