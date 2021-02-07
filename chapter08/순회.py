#전위 순회
def preorder(n):
    if n is not None:
        print(n.data, end = ' ') #먼저 루트노드 처리
        preorder(n.left) #왼쪽
        preorder(n.right) #오른쪽

#중위 순회
def inorder(n):
    if n is not None:
        inorder(n.left) #먼저 왼쪽
        print(n.data, end = ' ') #루트노드 처리
        inorder(n.right)

#후위 순회
def postorder(n):
    if n is not None:
        postorder(n.left)
        postorder(n.right)
        print(n.data, end = ' ') #마지막에 루트노드 처리
