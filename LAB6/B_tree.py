class Node:
    def __init__(self):
        self.keys = []
        self.children = [None]


class BTree:
    def __init__(self, max_children):
        self.max_children = max_children
        self.max_keys = max_children - 1
        self.root = Node()

    def add_to_node(self, node, key, child=None):
        idx = 0
        while idx < len(node.keys) and key > node.keys[idx]:
            idx += 1
        node.keys.insert(idx, key)
        node.children.insert(idx + 1, child)

        if len(node.keys) > self.max_keys:
            middle = len(node.keys) // 2
            middle_key = node.keys[middle]

            new_node = Node()
            new_node.keys = node.keys[middle + 1:]
            new_node.children = node.children[middle + 1:]

            node.keys = node.keys[:middle]
            node.children = node.children[:middle + 1]
            return middle_key, new_node
        return None
    
    def insert_recursive(self, node, key):
        idx = 0
        while idx < len(node.keys) and node.keys[idx] < key:
            idx += 1
        if node.children[0] is None:
            return self.add_to_node(node, key)
        else:
            split_result = self.insert_recursive(node.children[idx], key)
            if split_result is not None:
                middle_key, new_node = split_result
                return self.add_to_node(node, middle_key, new_node)
            return None

    def insert(self, key):
        split_result = self.insert_recursive(self.root, key)
        if split_result is not None:
            middle_key, new_node = split_result
            new_root = Node()
            new_root.keys = [middle_key]
            new_root.children = [self.root, new_node]
            self.root = new_root
    


    def print_tree(self):
        print("==============")
        self._print_tree(self.root, 0)
        print("==============")

    def _print_tree(self, node, lvl):
        if node!=None:
            for i in range(len(node.keys) + 1): 	                	
                self._print_tree(node.children[i], lvl+1)
                if i<len(node.keys):
                    print(lvl*'  ', node.keys[i])



def main():
    Tree = BTree(4)
    list = [5, 17, 2, 14, 7, 4, 12, 1, 16, 8, 11, 9, 6, 13, 0, 3, 18 , 15, 10, 19]
    for i in list:
        Tree.insert(i)
    Tree.print_tree()
    Tree2 = BTree(4)
    for i in range(20):
        Tree2.insert(i)
    Tree2.print_tree()
    for i in range(20, 200):
        Tree2.insert(i)
    Tree2.print_tree()
    Tree3 = BTree(6)
    for i in range(200):
        Tree3.insert(i)
    Tree3.print_tree()

if __name__ == "__main__":
    main()

    
