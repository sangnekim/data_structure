def quick_sort(A, left, right):
    if left < right:
        q = partition(A, left, right) #좌우로 분할
        quick_sort(A, left, q-1)
        quick_sort(A, q+1, right)

def partition(A, left, right):
    low = left + 1
    high = right
    pivot = A[left] #피벗 설정
    while (low <= high):
        while low <= high and A[low] < pivot:
            low += 1
        while high >= left and A[high] > pivot:
            high -= 1

        if low < high: #선택된 두 레코드 교환
            A[low],A[high] = A[high],A[low]

    A[left], A[high] = A[high],A[left] #마지막으로 high와 피벗 항목 교환
    return high #피벗의 위치 반환
