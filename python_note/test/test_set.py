# 집합의 특징
# (1) 중복 허용하지 않음
# (2) 순서가 없음

# 리스트 혹은 문자열을 이용해 초기화{} : set()함수 사용
# 데이터 조회 및 수정에 있어서 O(1)의 시간에 처리 가능

# 리스트로 초기화
data = set([1, 1, 2, 3, 4, 4, 5])
print(data)

# 직접 초기화
data = {1, 1, 2, 3, 4, 4, 5}
print(data)

# 연산: 합집합(|) / 교집합(&) / 차집합(-)
a_list = [1, 2, 3, 4, 5]
b_list = [3, 4, 5, 6, 7]
a_set = set(a_list)
b_set = set(b_list)
print(a_set | b_set) #합집합
print(a_set & b_set) #교집합
print(a_set - b_set) #차집합


data_list = [1, 2, 3]
data_set = set(data_list)
print(data_set)

# 새로운 원소 추가 : add
data_set.add(4)
print(data_set)

# 새로운 원소 여러개 추가 : update
data_set.update([5, 6])
print(data)

# 특정한 값을 갖는 원소 삭제 : remove
data_set.remove(3)
print(data_set)