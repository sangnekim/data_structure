#순환 알고리즘
def factorial(n):
    if n == 1:
        return 1
    else:
        return n*factorial(n-1)

#반복 알고리즘
def factorial(n):
    result = 1
    for k in range(n,0,-1):
        result = result*k
    return result
