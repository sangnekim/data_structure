#이진탐색트리 삽입연산 (노드를 삽입함): 순환구조
def insert_bst(r, n):
    if n.key < r.key:
        if r.left is None:
            r.left = n
            return True
        else:
            return insert_bst(r.left, n)
    elif n.key > r.key:
        if r.right is None:
            r.right = n
            return True
        else:
            return insert_bst(r.right, n)
    else: #키가 중복되면 삽입하지 않음
        return False
