# 리스트
# 대괄호[] 안에 원소를 넣어 초기화
# 쉼표(,)로 원소 구분
# 비어있는 리스트 선언은 list()혹은 간단히 []를 이용

# (1) Indexing
# : 리스트의 원소에 접근할 때는 인덱스 값을 괄호에 넣는다(인덱스는 0부터)
# : 인덱스가 양의 정수인 경우, 앞에서부터 탐색(0부터 시작)
# : 인덱스가 음의 정수인 경우, 뒤에서부터 거꾸로 탐색(-1부터 시작)
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a)
print(a[3]) # 4번째 원소 출력
print(a[-3]) # 뒤에서 3번째 원소 출력

# 크기가 n이고 모든 값이 0인 1차원 리스트 초기화
n = 10
a = [0]*n  
print(a)

# (2) Slicing
# : 연속적인 위치를 갖는 원소들을 가져와야 할 경우
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a[1:4]) # a[1] ~ a[3]까지 출력

# (3) List comprehension
# : 대괄호 안에 조건문과 반복문을 적용하여 리스트 초기화 가능
# 0~49까지의 수를 포함하는 리스트
array = [i for i in range(50)] 
print(array)

# 0~49까지의 수 중 홀수들을 포함하는 리스트
array = [i for i in range(50) if i%2 == 1] 
print(array)

# List comprehension 적용 안한 경우
array = []
for i in range(50):
    if(i % 2 == 1):
        array.append(i)
print(array)

# 2차원 리스트 초기화할 때 List comprehension이 효과적
n=4
m=3
array = [[0] * m for _ in range(n)] # N x M 사이즈 2차원 리스트
print(array)

# 반복을 수행하되, 반복을 위한 변수의 값을 무시하고자 할 때 _사용
# ex) Hello World 5번 출력하기
for _ in range(5):
    print("Hello World!")



# methods
# (1) arr.append(val) : arr의 맨 뒤에 val을 삽입 : O(1)
# (2) arr.sort() : arr을 오름차순으로 정렬 : O(NlogN)
#     arr.sort(reverse = True) : 내림차순 정렬 : O(NlogN)
# (3) arr.reverse() : arr의 원소 순서를 뒤집음 : O(N)
# (4) arr.insert(i, val) : arr[i]에 val을 삽입 : O(N)
# (5) arr.count(val) : arr에서 val과 같은 값을 갖는 데이터 개수 측정 : O(N)
# (6) arr.remove(val) : arr에서 val과 같은 값을 갖는 데이터 제거(여러개면 하나만 제거) : O(N)

a = [1, 4, 3]
print("기본 리스트: ", a)

a.append(2)
print("삽입: ", a)

a.sort()
print("오름차순 정렬: ", a)

a.sort(reverse=True)
print("내림차순 정렬: ", a)

a.reverse()
print("원소 뒤집기: ", a)

a.insert(2, 3)
print("index 2에 3을 추가: ", a)

print("값이 3인 데이터 개수: ", a.count(3))

a.remove(1)
print("값이 1인 데이터 제거: ", a)


# 리스트에서 특정 값을 가지는 원소 "모두" 제거
a = [1, 2, 3, 4, 5, 5, 5]
remove_set = {3, 5}

# remove_set에 포함되지 않은 값만을 result로 저장
result = [i for i in a if i not in remove_set]
print("a: ", a)
print("result: ", result) # 3, 5가 삭제됨