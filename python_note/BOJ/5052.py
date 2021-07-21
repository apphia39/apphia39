t = int(input())

for _ in range(t):
    n = int(input())
    phone = []
    flag = 0
    
    for _ in range(n):
        num = input()
        phone.append(num)
    
    # 사전순으로 정렬해두면 phone[i]와 phone[i+1]만 비교하면 됨
    phone.sort()
    
    for i in range(len(phone) - 1):
        if phone[i+1].find(phone[i]) == 0:
            print("NO")
            flag = 1
            break
    
    if flag == 0:
        print("YES")