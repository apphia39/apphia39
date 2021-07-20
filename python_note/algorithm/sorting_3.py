# O(nlogn) - 분할정복
# 3. 퀵 정렬: 기준 데이터 설정하고, 그 기준보다 큰 데이터와 작은 데이터의 위치를 바꾸는 방법
# 첫 번째 데이터를 기준 데이터(pivot)으로 설정
# 왼쪽에서부터 pivot보다 큰 데이터 선택, 오른쪽에서부터 pivot보다 작은 데이터 선택
# 이 상태에서 두 데이터의 위치 변경
# 왼쪽에서부터 pivot보다 큰 값 탐색, 오른쪽에서부터 pivot보다 작은 값 탐색하면서 갈 때, 왼쪽(i) 오른쪽(j) 위치가 엇갈리는 경우(j>i인 경우), 피벗과 작은 데이터의 위치를 서로 변경
# 최악의 경우 O(N^2)의 시간 복잡도를 가질 수 있다.

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(arr, start, end):
    if start >= end: # 원소가 1개인 경우 stop
        return
        
    pivot = start
    left = start + 1
    right = end

    while left <= right:
        # pivot보다 큰 값 찾기
        while left<=end and array[left] <= array[pivot]:
            left += 1
        # pivot보다 작은 값 찾기
        while right>start and array[right] > array[pivot]:
            right -= 1
        if left > right:
            array[pivot], array[right] = array[right], array[pivot]
        else:
            array[left], array[right] = array[right], array[left]
    
    pivot = right
    quick_sort(array, start, pivot-1)
    quick_sort(array, pivot+1, end)

quick_sort(array, 0, len(array)-1)
print(array)