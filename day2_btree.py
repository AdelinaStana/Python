'''
create btree
root.add(key)
root.print()
todo: foreach (Node node in root) => print(node.key)
'''

'''def __iter__(self):
    self.n = 0
    self.nodes_list = self.inorder([])
    return self

def __next__(self):
    self.n += 1
    if self.n <= len(self.nodes_list):
        return self.nodes_list[self.n - 1]
    else:
        raise StopIteration()'''


class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def add(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.add(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.add(data)
        else:
            self.data = data

    def inorder(self):
        if self.left:
            self.left.inorder()
        print(self.data)
        if self.right:
            self.right.inorder()

    def __iter__(self):
        if self.left:
            yield from self.left
        yield self
        if self.right:
            yield from self.right


if __name__ == '__main__':
    root = Node(None)
    root.add(8)
    root.add(2)
    root.add(15)
    root.add(1)
    root.add(5)
    root.add(4)
    root.add(7)
    root.add(3)

    root.inorder()
    print("___________________________")

    for n in root:
        print(n.data)

