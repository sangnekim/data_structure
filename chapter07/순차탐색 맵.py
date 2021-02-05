class SequentialMap:
    def __init__(self):
        self.table = []

    def size(self):
        return len(self.table)

    def display(self, msg):
        print(msg)
        for entry in self.table:
            print(" ", entry)

    def insert(self, key, value):
        self.table.append(Entry(key, value))

    def search(self, key):
        pos = sequential_search(self.table, key, 0, self.size()-1)
        if pos is not None:
            return self.table[pos]
        else:
            return None

    def delete(self, key):
        for i in range(self.size()):
            if self.table[i].key == key:
                self.table.pop(i)
                return
