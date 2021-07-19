# 문자열 변수 초기화는 큰따옴표(")나 작은따옴표(') 사용
# 전체 문자열을 큰 따옴표로 구성하는 경우, 내부적으로 작은따옴표를 포함할 수 있음
# 전체 문자열을 작은 따옴표로 구성하는 경우, 내부적으로 큰 다옴표를 포함할 수 있음
# 혹은 백슬래시(\) 사용하면 원하는만큼 큰따옴표나 작은 따옴표 포함시킬 수 있음

str = "Hello World!"
print(str)

str = "Don't you know \"Python\"?"
print(str)

# 문자열에 덧셈(+), 곱셈(*)연산 사용 가능
# indexing, slicing 가능
# 문자열은 특정 인덱스의 문자를 바꿀 수 없음

a = "Hello"
b = "World!"
print(a+" "+b)

a = "String"
print(a*3)

a = "ABCDEF"
print(a[2:4]) # C, D 출력