class Tree:
    def __init__(self):
        self.root = None

    def search(self, key):
        current = self.root
        while current is not None:
            if current.key == key:
                return current.val
            elif current.key > key:
                current = current.left
            elif current.key < key:
                current = current.right
        return None
    
    def insert(self, key, data):
        self.root = self.__insert_rec(self.root, key, data)

    def __insert_rec(self, node, key, data):
        if not node:
            return Node(key, data)
        
        if key < node.key:
            node.left = self.__insert_rec(node.left, key, data)
        elif key > node.key:
            node.right = self.__insert_rec(node.right, key, data)
        else:
            node.val = data 
            return node
        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
        balance = self.get_balance(node)
        if balance > 1 and key < node.left.key:
            return self.rotate_right(node)
        if balance < -1 and key > node.right.key:
            return self.rotate_left(node)
        if balance > 1 and key > node.left.key:
            node.left = self.rotate_left(node.left)
            return self.rotate_right(node)
        if balance < -1 and key < node.right.key:
            node.right = self.rotate_right(node.right)
            return self.rotate_left(node)
        return node
    
    def delete(self, key):
            self.root = self.__delete_rec(self.root, key)

    def __delete_rec(self, node, key):
        if node is None:
            return node

        if key < node.key:
            node.left = self.__delete_rec(node.left, key)
        elif key > node.key:
            node.right = self.__delete_rec(node.right, key)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            temp = self.__get_min_node(node.right)
            node.key = temp.key
            node.val = temp.val
            node.right = self.__delete_rec(node.right, temp.key)

        balance = self.get_balance(node)
        if balance > 1 and self.get_balance(node.left) >= 0:
            return self.rotate_right(node)
        if balance > 1 and self.get_balance(node.left) < 0:
            node.left = self.rotate_left(node.left)
            return self.rotate_right(node)
        if balance < -1 and self.get_balance(node.right) >= 0:
            return self.rotate_left(node)
        if balance < -1 and self.get_balance(node.right) < 0:
            node.right = self.rotate_right(node.right)
            return self.rotate_left(node)
        return node
    
    def __get_min_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current
        
    def print_tree(self):
        print("==============")
        self.__print_tree(self.root, 0)
        print("==============")

    def __print_tree(self, node, lvl):
        if node!=None:
            self.__print_tree(node.right, lvl+5)

            print()
            print(lvl*" ", node.key, node.val)
     
            self.__print_tree(node.left, lvl+5)
    
    def print_as_list(self):
        self.__print_in_order(self.root)
        print()

    def __print_in_order(self, node):
        if node is not None:
            self.__print_in_order(node.left)
            print(f'{node.key} {node.val},', end="")
            self.__print_in_order(node.right)

    def get_height(self, node):
        if not node:
            return 0
        return node.height

    def get_balance(self, node):
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    def rotate_right(self, y):
            x = y.left
            T = x.right

            x.right = y
            y.left = T

            y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
            x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))
            return x

    def rotate_left(self, x):
        y = x.right
        T = y.left

        y.left = x
        x.right = T

        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y

class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.left = None
        self.right = None
        self.height = 1


def main():
    BST = Tree()
    BST.insert(50, 'A')
    BST.insert(15, 'B')
    BST.insert(62, 'C')
    BST.insert(5, 'D')
    BST.insert(2, 'E')
    BST.insert(1, 'F')
    BST.insert(11, 'G')
    BST.insert(100, 'H')
    BST.insert(7, 'I')
    BST.insert(6, 'J')
    BST.insert(55, 'K')
    BST.insert(52, 'L')
    BST.insert(51, 'M')
    BST.insert(57, 'N')
    BST.insert(8, 'O')
    BST.insert(9, 'P')
    BST.insert(10, 'R')
    BST.insert(99, 'S')
    BST.insert(12, 'T')
    BST.print_tree()
    BST.print_as_list()
    print(BST.search(10))
    BST.delete(50)
    BST.delete(52)
    BST.delete(11)
    BST.delete(57)
    BST.delete(1)
    BST.delete(12)
    BST.insert(3, 'AA')
    BST.insert(4, 'BB')
    BST.delete(7)
    BST.delete(8)
    BST.print_tree()
    BST.print_as_list()

if __name__ == "__main__":
    main()