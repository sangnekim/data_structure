def reBalance(parent):
    hDiff = calc_height_diff(parent)

    if hDiff > 1:
        if calc_height_diff(parent.left) > 0:
            parent = rotateLL(parent)
        else:
            parent = rotateLR(parent)
    elif hDiff < -1:
        if calc_height_diff(parent.right) < 0:
            parent = rotateRR(parent)
        else:
            parent = rotateRL(parent)
    return parent

def rotateLL(A):
    B = A.left
    A.left = B.right
    B.right = A
    return B #새로운 루트 B를 반환

def rotateRR(A):
    B = A.right
    A.right = B.left
    B.left = A
    return B # 새로운 루트 B 반환

def rotateRL(A):
    B = A.right
    A.right = rotateLL(B)
    return rotateRR(A)

def rotateLR(A):
    B = A.left
    A.left = rotateRR(B)
    return rotateLL(A)

#8장에서 구현한 함수
def calc_height(n):
    if n is None: # 공백트리 --> 0 반환
        return 0
    hLeft = calc_height(n.left) # 왼쪽 트리의 높이
    hRight = calc_height(n.right) #오른쪽 트리의 높이
    if (hLeft > hRight): #더 높은 높이에 1을 더해 반환
        return hLeft + 1
    else:
        return hRight + 1

def calc_height_diff(n):
    if n is None:
        return 0
    return calc_height(n.left) - calc_height(n.right)
