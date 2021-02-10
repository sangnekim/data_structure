class AVLMap(BSTMap):
    def __init__(self):
        super().__init__()

    def insert(self, key, value = None):
        n = BSTNode(key, value)
        if self.isEmpty():
            self.root = n
        else:
            self.root = insert_avl(self.root, n)

    def display(self, msg = 'AVLMap :'):
        print(msg, end = '')
        levelorder(self.root)
        print()
