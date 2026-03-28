import random

class Elem:
    def __init__(self, key, val, levels):
        self.key = key
        self.val = val
        self.levels = levels
        self.tab = [None] * levels

class skip_list:
    def __init__(self, max_height):
        self.max_height = max_height
        self.head = Elem(None, None, self.max_height)

    def randomLevel(self, p = 0.5):
        lvl = 1   
        while random.random() < p and lvl < self.max_height:
            lvl = lvl + 1
        return lvl
    
    def search(self, key):
        node = self.head
        for lvl in range(self.max_height - 1, -1, -1):
            while node.tab[lvl] is not None and node.tab[lvl].key < key:
                node = node.tab[lvl]
        node = node.tab[0]
        if node is not None and node.key == key:
            return node.val
        else:
            return None

    def insert(self, data, key):
        node = self.head
        update = [None] * self.max_height
        for lvl in range(self.max_height - 1, -1, -1):
            while node.tab[lvl] is not None and node.tab[lvl].key < key:
                node = node.tab[lvl]
            update[lvl] = node
        node = node.tab[0]
        if node is not None and node.key == key:
            node.val = data
            return
        else:
            lvl = self.randomLevel()
            new_node = Elem(val = data, key = key, levels = lvl)
            for i in range(lvl):
                new_node.tab[i] = update[i].tab[i]
                update[i].tab[i] = new_node
            return

    def remove(self, key):
        node = self.head
        update = [None] * self.max_height
        for lvl in range(self.max_height - 1, -1, -1):
            while node.tab[lvl] is not None and node.tab[lvl].key < key:
                node = node.tab[lvl]
            update[lvl] = node
        node = node.tab[0]
        if node is not None and node.key == key:
            for i in range(self.max_height):
                if update[i].tab[i] != node:
                    break
                update[i].tab[i] = node.tab[i]

    def __str__(self):
        node = self.head.tab[0]
        str = '{'
        while node is not None:
            str += f"{node.key}:{node.val}"
            node = node.tab[0]
            if node is not None:
                    str += ', '
        str += '}'
        return str
    
    def displayList_(self):
        node = self.head.tab[0]  
        keys = []                        
        while node is not None:
            keys.append(node.key)
            node = node.tab[0]

        for lvl in range(self.max_height - 1, -1, -1):
            print(f"{lvl}  ", end=" ")
            node = self.head.tab[lvl]
            idx = 0
            while node is not None:
                while node.key > keys[idx]:
                    print(end=5*" ")
                    idx += 1
                idx += 1
                print(f"{node.key:2d}:{node.val:2s}", end="")
                node = node.tab[lvl]
            print()


def main():
    random.seed(42)
    List = skip_list(5)
    values = [chr(i) for i in range(65, 65 + 15)]
    for idx, val in enumerate(values):
        List.insert(val, idx + 1)
    
    List.displayList_()
    print(List.search(2))
    List.insert('Z', 2)
    print(List.search(2))
    for i in [5,6,7]:
        List.remove(i)
    print(List)
    List.insert('W', 6)
    print(List)

if __name__ == "__main__":
    main()