def sequential_search(A, key, low, high): # key:탐색키, low~high: 탐색 범위
    for i in range(low, high+1):
        if A[i].key == key:
            return i
    return None
