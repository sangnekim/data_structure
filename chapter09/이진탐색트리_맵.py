class BSTMap():
    def __init__(self):
        self.root = None #트리의 루트 노드

    def isEmpty(self):
        return self.root == None

    def claer(self):
        self.root = None

    def size(self):
        return count_node(self.root)

    def search(self, key):
        return search_bst(self.root, key)

    def searchValue(self, key):
        return search_value_bst(self.root, key)

    def findMax(self):
        return search_max_bst(self.root)

    def findMin(self):
        return search_min_bst(self.root)

    def insert(self, key, value = None):
        n = BSTNode(key, value) #새로운 노드 생성
        if self.isEmpty(): #공백이면 루트노드로 삽입
            self.root = n
        else: #공백이 아니면
            insert_bst(self.root, n)

    def delete(self, key):
        self.root = delete_bst(self.root, key)

    def display(self, msg = 'BSTMap :'):
        print(msg, end = '')
        inorder(self.root)
        print()
