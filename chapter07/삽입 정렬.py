def insertion_sort(A):
    n = len(A)
    for i in range(1,n):
        key = A[i] # key는 정렬된 부분에 삽입할 원소
        j = i-1
        while j>= 0 and A[j] > key: # key보다 큰 원소들을 뒤로 한 칸씩 이동
            A[j+1] = A[j]
            j -=1
        A[j+1] = key # key 보다 큰 정렬된 원소들 앞으로 삽입
        printStep(A, i)
