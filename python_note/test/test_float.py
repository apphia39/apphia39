a = 12.12    #양의실수
print(a)

a = -1.2     #음의실수
print(a)

a = 5.       #5.0은 뒤에 0 생략 가능
print(a)

a = -.7      #-0.7은 앞에 0 생략 가능
print(a)

a = 7e7      #7 * 10^7
print(a)

a=394e-3     #394 * 10^(-3)
print(a)

#유도한 결과를 얻지 못하는 경우가 있을 수 있음
a=0.3+0.6    #a != 0.9
print(a)
if a==0.9:
    print(True)
else:
    print(False)

#따라서 round()함수를 사용
a=0.3+0.6
print(round(a, 1))
if round(a, 1) == 0.9:
    print(True)
else: 
    print(False)