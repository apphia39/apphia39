# Key-Value 쌍을 데이터로 갖는다.
# Hash table을 이용하므로 데이터의 조회 및 수정에 있어서 O(1) 시간에 처리 가능

data = dict()
data['사과'] = 'Apple'
data['바나나'] = 'Banana'
data['코코넛'] = 'Coconut'

print(data)

if '사과' in data:
    print("'사과'를 키로 갖는 데이터가 존재합니다.")

# 키만 출력
print(data.keys())
for i in data.keys():
    print("key: ", i)

# 값만 출력
print(data.values())
for i in data.values():
    print("value: ", i)

# 동시 출력
for key, value in data.items():
    print("key: ", key, "value: ", value)


# 초기화
b = {
    '사과' : 'apple',
    '바나나' : 'banana',
    '코코넛' : 'coconut'
}
print(b)
