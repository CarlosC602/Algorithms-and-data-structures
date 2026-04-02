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
        if self.root is None:
            self.root = Node(key, data)
            return
        current = self.root
        parent = None
        while current is not None:
            if current.key == key:
                current.val = data
                return
            parent = current
            if current.key > key:
                current = current.left
            elif current.key < key:
                current = current.right
        if parent.key > key:
            parent.left = Node(key, data)
            return
        else:
            parent.right = Node(key, data)
            return
    
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

    def height(self):
        return self.__height_rec(self.root)
    
    def __height_rec(self, node):
        if node is None:
            return -1
        left_height = self.__height_rec(node.left)
        right_height = self.__height_rec(node.right)
        return max(left_height, right_height) + 1    



class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.left = None
        self.right = None


def main():
    BST = Tree()
    BST.insert(50, 'A')
    BST.insert(15, 'B')
    BST.insert(62, 'C')
    BST.insert(5, 'D')
    BST.insert(20, 'E')
    BST.insert(58, 'F')
    BST.insert(91, 'G')
    BST.insert(3, 'H')
    BST.insert(8, 'I')
    BST.insert(37, 'J')
    BST.insert(60, 'K')
    BST.insert(24, 'L')
    BST.print_tree()
    BST.print_as_list()
    print(BST.search(24))
    BST.insert(20, 'AA')
    BST.insert(6, 'M')
    BST.delete(62)
    BST.insert(59, 'N')
    BST.insert(100, 'P')
    BST.delete(8)
    BST.delete(15)
    BST.insert(55, 'R')
    BST.delete(50)
    BST.delete(5)
    BST.delete(24)
    print(BST.height())
    BST.print_as_list()
    BST.print_tree()

if __name__ == "__main__":
    main()