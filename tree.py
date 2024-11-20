class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.count = 1
        self.left = None
        self.right = None

    def __str__(self):
        return f"data: {self.data}\ncount: {self.count}\nleft: {self.left.data if self.left else None}\nright: {self.right.data if self.right else None}\n"

class Tree:
    def __init__(self):
        self.root = None


    def isEmpty(self):
        return self.root == None
    
    def insert(self, data):
        newnode = Node(data)

        if (self.isEmpty()):
            self.root = newnode
            return
        
        self.recursiveInsert(self.root, newnode)
    
    def recursiveInsert(self, node: Node, newnode: Node):

        if (newnode.data < node.data):
            
            if (not node.left):
                node.left = newnode
            else:
                self.recursiveInsert(node.left, newnode)

        elif (newnode.data > node.data):

            if (not node.right):
                node.right = newnode
            else:
                self.recursiveInsert(node.right, newnode)

    
    def print_in_order(self, node):
        if (self.isEmpty()):
            return print("Tree is empty")

        if (not node):
            return

        self.print_in_order(node.left)
        print(node.data)
        self.print_in_order(node.right)

    def max_depth(self, node):
        if node is None:
            return 0
        
        left_depth = self.max_depth(node.left)
        right_depth = self.max_depth(node.right)
        
        return max(left_depth, right_depth) + 1
        
        
        

tree = Tree()

tree.insert(2)
tree.insert(1)
tree.insert(3)
tree.insert(4)
tree.print_in_order(tree.root)
print(tree.max_depth(tree.root))

    
