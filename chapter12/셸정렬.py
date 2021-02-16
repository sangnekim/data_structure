#gap만큼 떨어진 요소들을 삽입 정렬. 정렬 범위는 first에서 last
def sortGapInsertion(A, first, last, gap):
    for i in range(first+gap, last+1, gap):
        key = A[i]
        j = i-gap
        while j >= first and key<A[j]: #삽입 위치를 찾음
            A[j+gap] = A[j] #항목 이동
            j = j- gap
        A[j+gap] = key #최종 위치에 삽입

def shell_sort(A):
    n = len(A)
    gap = n//2
    while gap > 0 :
        if gap%2 == 0:
            gap += 1
        for i in range(gap):
            sortGapInsertion(A,i,n-1, gap)
        print('    Gap=', gap, A)
        gap = gap//2
