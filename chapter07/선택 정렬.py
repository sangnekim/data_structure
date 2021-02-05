def selection_sort(A):
    n = len(A)
    for i in range(n-1):
        least = i
        for j in range(i+1, n):
            if A[j] < A[least]:
                least = j #최소항목 갱신
        A[i], A[least] = A[least], A[i] #배열 항목 교환
        printStep(A, i+1) #중간 과정 출력용
