def dp_quick_sort(A, low, high):
    if low < high:
        lp, rp = partitionDP(A, low, high) #좌우 피벗의 인덱스를 반환
        dp_quick_sort(A, low, lp-1)
        dp_quick_sort(A, lp+1, rp-1)
        dp_quick_sort(A, rp+1, high)

def partitionDP(A, low, high):
    if A[low] > A[high]: #오른쪽 피벗은 왼쪽 피벗보다 작지 않아야 함
        A[low], A[high] = A[high], A[low]

    j = low+1
    g = high-1
    k = low+1
    lpVal = A[low] #왼쪽 피벗값
    rpVal = A[high] #오른쪽 피벗값
    while k <= g:
        if A[k] < lpVal: #A[k]가 왼쪽 피벗보다 작으면
            A[k],A[j] = A[j], A[k] #교환
            j += 1

        elif A[k] >= rpVal:
            while A[g] > rpVal and k < g: #g의 위치 찾기
                g -= 1
            A[k], A[g] = A[g], A[k]
            g -= 1

            if A[k] < lpVal: #변경된 A[k]가 왼쪽 피벗보다 작으면
                A[k],A[j] = A[j],A[k] #다시 교환
                j += 1
            k += 1

    j -= 1
    g += 1
    A[low],A[j] = A[j], A[low]
    A[high], A[g] = A[g], A[high]

    return j, g #왼쪽과 오른쪽 피벗의 인덱스
