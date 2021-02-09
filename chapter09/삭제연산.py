#삭제할 노드가 단말인 경우
def delete_bst_case1(parent, node, root):
    if parent is None: #삭제할 단말 노드가 루트이면
        root = None  #공백 트리가 됨
    else:
        if parent.left == node:
            parent.left = None
        else:
            parent.right = None

    return root #root가 변경될 수도 있으므로 반환

#삭제할 노드가 하나의 자식을 갖는 경우
def delete_bst_case2(parent, node, root):
    if node.left is not None: #삭제할 노드가 왼쪽 자식만 가짐
        child = node.left
    else: #삭제할 노드가 오른쪽 자식만 가짐
        child = node.right

    if node == root:
        root = child
    else:
        if node is parent.left:
            parent.left = child
        else:
            parent.right = child

    return root #root가 변경될 수도 있으므로 반환

#두 개의 자식을 모두 갖는 경우
def delete_bst_case3(parent, node, root):
    succp = node #후계장의 부모 노드
    succ = node.right #후계자 노드
    while (succ.left != None): #후계자와 부모노드 탐색
        succp = succ
        succ = succ.left

    if (succp.left == succ): #후계자가 왼쪽 자식이면
        succp.left = succ.right #후계자의 오른쪽 자식 연결
    else: #후계자가 오른쪽 자식이면
        succp.right = succ.right #후계자의 왼쪽 자식 연결

    #후계자의 키와 값을 삭제할 노드에 복사
    node.key = succ.key
    node.value = succ.value
    node = succ

    return root #일관성을 위해 root 반환

#이진탐색트리 삭제연산
def delete_bst(root, key):
    if root == None:
        return None

    parent = None
    node = root
    while node != None and node.key != key:
        parent = node
        if key < node.key:
            node = node.left
        else:
            node = node.right

    if node == None: #삭제할 노드가 없음
        return None
    if node.left == None and node.right == None: #case1
        root = delete_bst_case1(parent, node, root)
    elif node.left == None or node.right == None: #case2
        root = delete_bst_case2(parent, node, root)
    else: #case3
        root = delete_bst_case3(parent, node, root)
    return root
