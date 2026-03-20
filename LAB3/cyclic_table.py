class cyclic_table:
    def __init__(self, size = 5):
        self.size = size
        self.tab = [None for _ in range(size)]
        self.read_idx = 0
        self.write_idx = 0

    def is_empty(self):
        return self.write_idx == self.read_idx
    
    def peek(self):
        if self.is_empty():
            return None
        return self.tab[self.read_idx]
    
    def dequeue(self):
        if self.is_empty():
            return None
        value = self.peek()
        self.tab[self.read_idx] = None
        self.read_idx = (self.read_idx + 1) % self.size
        return value

    def enqueue(self, data):
        self.tab[self.write_idx] = data
        self.write_idx = (self.write_idx + 1) % self.size
        if self.write_idx == self.read_idx:
            new_tab = [None for _ in range(2 * self.size)]
            for i in range(self.size):
                old_idx = (self.read_idx + i) % self.size
                new_tab[i] = self.tab[old_idx]
            self.tab = new_tab
            self.read_idx = 0
            self.write_idx = self.size
            self.size *= 2

    def __str__(self):
        string = '['
        idx = (self.read_idx) % self.size
        while idx != self.write_idx:
            string += f'{self.tab[idx]}'
            if (idx + 1) % self.size != self.write_idx:
                string += ','
            idx = (idx + 1) % self.size
        string += ']'
        return string
    
    def print_(self):
        string = '['
        for i in range(self.size):
            string += str(self.tab[i])
            if i < self.size - 1:
                string += ','
        string += ']'
        return string

def main():
    table = cyclic_table()
    table.enqueue(0)
    table.enqueue(1)
    print(table.dequeue())
    print(table.peek())
    table.enqueue(2)
    table.enqueue(3)
    table.enqueue(4)
    print(table.dequeue())
    print(table)
    table.enqueue(5)
    table.enqueue(6)
    table.enqueue(7)
    table.enqueue(8)
    print(table.print_())
    while table.read_idx != table.write_idx:
        print(table.dequeue())
    print(table)

if __name__ == "__main__":
    main()
