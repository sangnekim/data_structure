MAX_VAL = 1000
def counting_sort(A):
    output = [0]*MAX_VAL
    count = [0]*MAX_VAL

    for i in A: #각 숫자별 빈도를 계산
        count[i] += 1

    for i in range(MAX_VAL): #count[i]가 출력 배열에서
        count[i] += count [i-1] #해당 숫자의 위치가 되도록 수정

    for i in range(len(A)):
        output[count[A[i]]-1] = A[i]
        count[A[i]] -= 1

    for i in range(len(A)):
        A[i] = output[i]
