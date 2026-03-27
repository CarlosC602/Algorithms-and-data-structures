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
        while True:
            idx = (base_idx + self.c1 * k + self.c2 * k ** 2) % self.size
            k += 1
            if self.tab[idx] is None or self.tab[idx].key == key:
                return idx
            if k == self.size:
                return None
            
    def search(self, key):
        base_idx = self.hash(key)
        if self.tab[base_idx] is not None and self.tab[base_idx].key == key:
            return self.tab[base_idx].val
        idx = self.resolve_collision(base_idx)
        if self.tab[idx] == None:
            return None
        else:
            return self.tab[idx].val
    
    def insert(self, val, key):
        idx = self.hash(key)
        if self.tab[idx] == None:
            self.tab[idx] = Elem(key, val)
            return
        if self.tab[idx].key == key:
            self.tab[idx].val = val
            return
        idx = self.resolve_collision(idx)
        if idx is None:
            return None, "Lack of space"
        if self.tab[idx] == None:
            self.tab[idx] = Elem(key, val)
            return
        if self.tab[idx].key == key:
            self.tab[idx].val = val
            return

    def remove(self, key):
        base_idx = self.hash(key)
        if self.tab[base_idx] is not None and self.tab[base_idx].key == key:
            self.tab[base_idx] = None
        idx = self.resolve_collision(base_idx)
        if self.tab[idx] != None:
            self.tab[idx] = None
        return

    def __str__(self):
        print("{")
        # for i in range(self.size):
