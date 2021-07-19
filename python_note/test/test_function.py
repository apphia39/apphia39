def add(a, b):
    return a+b

def subtract(a, b):
    return a-b

def product(a, b):
    return a*b

def power(a, b):
    return a**b

def root(a):
    return a**0.5

def divide(a, b):
    return a/b

def remainder(a, b):
    return a%b

def quotient(a, b):
    return a//b

def calc(a, b):
    return add(a, b), subtract(a, b), product(a, b), divide(a, b)



# function call
print(power(3, 2))
a, b, c, d = calc(6, 3)
print(a, b, c, d)


# lambda 매개변수들 : 실행문
# ex) add(3, 7)과 동일한 결과
print((lambda a, b: a+b)(3, 7))
# 또는
result = lambda a, b: a+b
print(result(3, 7))

# 내장 함수에서 자주 사용되는 lambda 함수
array = [('홍길동', 50), ('이순신', 32), ('아무개', 74)]

def my_key(x):   
    return x[1] # 튜플의 2번째 속성을 반환
print(sorted(array, key=my_key)) # 튜플의 2번째 속성값에 따라 오름차순 정렬

print(sorted(array, key=lambda x: x[1])) # lambda 사용: 튜플의 2번째 속성값에 따라 오름차순 정렬

# 여러개의 리스트에 적용 : lambda
list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]
result = map(lambda a, b: a+b, list1, list2) 
print(list(result))