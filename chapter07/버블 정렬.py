def bubble_sort(A):
    n = len(A)
    for i in range(n-1, 0, -1):
        bChanged = False
        for j in range(i):
            if (A[j] > A[j+1]):
                A[j], A[j+1] = A[j+1], A[j] # 교환
                bChanged = True

        if not bChanged: # 교환이 없으면 종료
            break
        printStep(A, n-i)
