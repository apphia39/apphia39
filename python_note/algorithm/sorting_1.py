# O(n^2)
# 1. 선택 정렬 : 처리되지 않은 데이터 중 가장 작은 데이터를 선택해 현재 범위의 맨 앞에 있는 데이터와 바꾸는 것을 반복
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
    min_idx = i
    for j in range(i, len(array)):
        if array[min_idx] >= array[j]:
            min_idx = j
    array[min_idx], array[i] = array[i], array[min_idx]

print(array)