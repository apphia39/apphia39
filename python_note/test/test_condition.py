# 조건문
score = 85

if score >= 90:
    print("학점: A")
elif score >= 80:
    print("학점: B")
elif score >= 70:
    print("학점: C")
else :
    print("학점: F")


a = 15
if 0 <= a and a <= 20:    # if 0 <= a <= 20 이라고 쓸 수도 있음
    print("True")
else:
    print("False")

a = 9
if a < 10:
    pass
else:
    print("a >= 10")
