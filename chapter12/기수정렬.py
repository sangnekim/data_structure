from queue import Queue

def radix_sort(A):
    queues = []
    for i in range(BUCKETS):
        queues.append(Queue())

    n = len(A)
    factor = 1 #1의 자리부터 시작
    for d in range(DIGITS):
        for i in range(n): #자릿수에 따라 큐에 삽입
            queues[(A[i]//factor)%10].put(A[i]) #숫자를 삽입
        i = 0
        for b in range(BUCKETS):
            while not queues[b].empty():
                A[i] = queues[b].get()
                i += 1
        factor *= 10 #그 다음 자리수로 간다.
        print('step', d+1, A)
