#반복 알고리즘
def power_item(x, n):
    result = 1.0
    for i in range(n):
        result = result*x
    return result

#순환 알고리즘
def power(x, n):
    if n == 0:
        return 1
    elif (n%2) == 0:
        return power(x*x, n//2)
    else:
        return x*power(x*x, (n-1)//2)
