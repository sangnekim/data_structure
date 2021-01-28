class Set:
    def __init__(self):
        self.items = []

    def size(self):
        return len(self.items)

    def display(self, msg):
        print(msg, self.items)

    def contains(self, item):
        return item in self.items

    def insert(self, elem):
        if elem not in self.items:
            self.items.append(elem)

    def delete(self, elem):
        if elem in self.items:
            self.items.remove(elem)

    def union(self, setB):
        setC = Set()
        setC.items = list(self.items)
        for elem in setB.items:
            setC.items.append(elem)
        return setC

    def intersect(self, setB):
        setC = Set()
        for elem in setB.items:
            if elem in self.items:
                setC.items.append(elem)
        return setC

    def difference(self, setB):
        setC = Set()
        for elem in self.items:
            if elem not in setB.items:
                setC.items.append(elem)
        return setC
