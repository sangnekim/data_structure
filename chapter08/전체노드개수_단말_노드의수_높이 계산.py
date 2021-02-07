#전체 노드개수
def count_node(n):
    if n is None:
        return 0
    else:
        return 1+count_node(n.left) + count_node(n.right)

#단말 노드 개수
def count_leaf(n):
    if n is None: #공백 트리 --> 0 반환
        return 0
    elif n.left is None and n.right is None: #단말노드 --> 1 반환
        return 1
    else: #비단말 노드: 좌우 서브트리의 결과 합을 반환
        return count_leaf(n.left) + count_leaf(n.right)

#트리의 높이
def calc_height(n):
    if n is None: # 공백트리 --> 0 반환
        return 0
    hLeft = calc_height(n.left) # 왼쪽 트리의 높이
    hRight = calc_height(n.right) #오른쪽 트리의 높이
    if (hLeft > hRight): #더 높은 높이에 1을 더해 반환
        return hLeft + 1
    else:
        return hRight + 1
