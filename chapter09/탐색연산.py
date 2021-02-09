#순환함수
def search_bst(n, key):
    if n == None:
        return None
    elif key == n.key:
        return n
    elif key < n.key:
        return search_bst(n.left, key)
    else:
        return search_bst(n.right, key)

#반복함수
def search_bst_iter(n, key):
    while n != None:
        if key == n.key:
            return n
        elif key < n.key:
            n = n.left
        else:
            n = n.right
    return None

#이진탐색트리 탐색연산(preorder사용): 값을 이용한 탐색
def search_value_bst(n, value):
    if n == None:
        return None
    elif value == n.value:
        return n
    res = search_value_bst(n.left, value) #왼쪽서브트리에서 탐색
    if res is not None: #성공하면 결과 반환
        return res
    else: #실패하면 오른쪽을 탐색해 결과 반환
        return search_value_bst(n.right, value)

#최대와 최소 노드 탐색
def search_max_bst(n):
    while n != None and n.right != None:
        n = n.right
    return n

def search_min_bst(n):
    while n != None and n.left != None:
        n = n.left
    return n
