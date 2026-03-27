DELETED = object()

class Elem:
    def __init__(self, key, val):
        self.key = key
        self.val = val

    def __str__(self):
        return f'{self.key}:{self.val}'

class static_tab:
    def __init__(self, size = 10, c1 = 1, c2 = 0):
        self.size = size
        self.tab = [None for _ in range(size)]
        self.c1 = c1
        self.c2 = c2

    def hash(self, data):
        if isinstance(data, str):
            key_val =  sum(ord(char) for char in data)
        else:
            key_val = data
        idx = key_val % self.size
        return idx
    
    def resolve_collision(self, base_idx, key):
        k = 1
        while k < self.size:
            idx = (base_idx + self.c1 * k + self.c2 * k ** 2) % self.size
            k += 1
            if self.tab[idx] is None:
                return idx
            if self.tab[idx] is not DELETED and self.tab[idx].key == key:
                return idx
        return None
            
    def search(self, key):
        base_idx = self.hash(key)
        if self.tab[base_idx] is not None and self.tab[base_idx].key == key and self.tab[base_idx] is not DELETED:
            return self.tab[base_idx].val
        idx = self.resolve_collision(base_idx, key)
        if idx is None or self.tab[idx] is None or self.tab[idx] is DELETED:
            return None
        return self.tab[idx].val
    
    def insert(self, val, key):
        idx = self.hash(key)
        if self.tab[idx] is None or self.tab[idx] is DELETED:
            self.tab[idx] = Elem(key, val)
            return
        if self.tab[idx].key == key:
            self.tab[idx].val = val
            return
        idx = self.resolve_collision(idx, key)
        if idx is None:
            return None, "Lack of space"
        if self.tab[idx] is None or self.tab[idx] is DELETED:
            self.tab[idx] = Elem(key, val)
            return
        if self.tab[idx].key == key:
            self.tab[idx].val = val
            return

    def remove(self, key):
        base_idx = self.hash(key)
        if self.tab[base_idx] is not None and self.tab[base_idx].key == key and self.tab[base_idx] is not DELETED:
            self.tab[base_idx] = None
        idx = self.resolve_collision(base_idx, key)
        if idx != None and self.tab[idx] != None and self.tab[idx].key == key and self.tab[idx] is not DELETED:
            self.tab[idx] = DELETED
        return

    def __str__(self):
        str = '{'
        for i in range(self.size):
            if self.tab[i] is not None:
                str += f'{self.tab[i].key}:{self.tab[i].val}'
                if i < self.size - 1:
                    str += ', '
            elif self.tab[i] is DELETED:
                str += 'DELETED, '
            else:
                str += 'None, '
        str += '}'
        return str

def main():
    def Test_1(c1 = 0, c2 = 1):
        numbers = [1,2,3,4,5,18,31,8,9,10,11,12,13,14,15]
        values = [chr(i) for i in range(65, 65 + 15)]
        Table_1 = static_tab(c1 = c1, c2 = c2, size = 13)
        for num, val in zip(numbers, values):
            Table_1.insert(val, num)
        print(Table_1)
        print(Table_1.search(5))
        print(Table_1.search(14))
        Table_1.insert('Z', 5)
        print(Table_1.search(5))
        Table_1.remove(5)
        print(Table_1)
        print(Table_1.search(31))
        return Table_1
    
    Table = Test_1()
    print("___________________________________________________________________________________________________________")
    Table.insert('W', 'test')
    print(Table)
    print("___________________________________________________________________________________________________________")

    def Test_2(c1 = 1, c2 = 0):
        Table_2 = static_tab(c1 = c1, c2 = c2, size = 13)
        numbers = [13 * i for i in range(1, 16)]
        values = [chr(i) for i in range(65, 65 + 15)]
        for num, val in zip(numbers, values):
            Table_2.insert(val, num)
        return print(Table_2)
    
    Test_2()
    print("___________________________________________________________________________________________________________")
    Test_2(0, 1)
    print("___________________________________________________________________________________________________________")
    Test_1(0, 1)


if __name__ == "__main__":
    main()
    
