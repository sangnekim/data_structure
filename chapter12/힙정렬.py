#다운 힙 수행 함수
def heapify(arr, n, i): #n: 배열의 길이, i: 다운힙을 진행하고자 하는 항목의 인덱스
    largest = i #i번째가 가장 크다고 하자
    l = 2*i + 1 #왼쪽 자식
    r = 2*i + 2 #오른쪽 자식

    if l < n and arr[i] < arr[l]: #교환조건 검사
        largest = l
    if r < n and arr[largest] < arr[r]: #교환조건 검사
        largest = r
    if largest != i: #교환이 필요하면
        arr[i], arr[largest] = arr[largest], arr[i] #교환
        heapify(arr, n ,largest) #순차적으로 자식노드로 내려감

def heapSort(arr):
    n = len(arr)
    print('i=', 0 ,arr)
    for i in range(n//2, -1, -1): #최대 힙을 만듦
        heapify(arr, n ,i)
        print("i=", i, arr)
    print()

    for i in range(n-1, 0, -1):
        arr[i],arr[0] = arr[0],arr[i] #루트를 뒤쪽으로 옮김. 교체
        heapify(arr, i, 0) #heap 조건을 맞춤
        print('i=', i ,arr)
