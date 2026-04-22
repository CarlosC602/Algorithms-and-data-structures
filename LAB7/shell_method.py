import time
import random

class Elem:
    def __init__(self, priority, data):
        self.priority = priority
        self.data = data
    def __gt__(self, other):
        return self.priority > other.priority
    def __repr__(self):
        return f"({self.priority}, '{self.data}')"
    
class Queue:
    def __init__(self, table_to_sort = None):
        if table_to_sort == None:    
            self.table = []
            self.size = 0
        else:
            self.table = table_to_sort
            self.size = len(table_to_sort)
            last_parent = (self.size - 2) // 2
            for i in range(last_parent, -1, -1):
                self.fix_down(i)

    def parent(self, i):
        return (i-1) // 2
    
    def left(self, i):
        return 2*i + 1

    def right(self, i):
        return 2*i + 2
    
    def is_empty(self):
        return self.size == 0
    
    def peek(self):
        if self.size == 0:
            return None
        else:
            return self.table[0]
        
    def dequeue(self):
        if self.is_empty() == True:
            return None
        max_elem = self.table[0]
        idx = self.size - 1
        self.table[0], self.table[idx] = self.table[idx], self.table[0]
        self.size -= 1
        self.fix_down(0)
        return max_elem

    def fix_down(self, idx = 0):
        while True:
            left = self.left(idx)
            right = self.right(idx)
            max_idx = idx

            if left < self.size:
                if self.table[left] > self.table[max_idx]:
                    max_idx = left
            
            if right < self.size:
                if self.table[right] > self.table[max_idx]:
                    max_idx = right

            if max_idx == idx:
                break

            else:
                self.table[max_idx], self.table[idx] = self.table[idx], self.table[max_idx]
            idx = max_idx

    def enqueue(self, element):
        if self.size == len(self.table):
            self.table.append(element)
            self.size += 1
            self.fix_up(self.size - 1)
        
        else:
            self.table[self.size] = element
            self.size += 1
            self.fix_up(self.size - 1)

    def fix_up(self, idx):
        while idx > 0:
            parent_idx = self.parent(idx)
            if self.table[idx] > self.table[parent_idx]:
                self.table[parent_idx], self.table[idx] = self.table[idx], self.table[parent_idx]
                idx = parent_idx
            else:
                break

    def print_tab(self):
        print ('{', end=' ')
        print(*self.table[:self.size], sep=', ', end = ' ')
        print( '}')

    def print_tree(self, idx, lvl):
        if idx<self.size:           
            self.print_tree(self.right(idx), lvl+1)
            print(2*lvl*'  ', self.table[idx] if self.table[idx] else None)           
            self.print_tree(self.left(idx), lvl+1)

def insertion_sort(table):
    size = len(table)
    for i in range (1, size):
        j = i
        while j > 0 and table[j-1] > table[j]:
            table[j - 1], table[j] = table[j], table[j - 1]
            j -= 1
    return table

def shell_method_engine(table, h):
    size = len(table)
    for x in range(h):
        for i in range(x + h, size, h):
            j = i
            while j >= h and table[j - h] > table[j]:
                table[j - h], table[j] = table[j], table[j - h]
                j -= h
    
def shell_method_classic(table):
    size = len(table)
    h = size // 2
    while h >= 1:
        shell_method_engine(table, h)
        h = h // 2
    return table

def shell_method_modified(table):
    size = len(table)
    h = 1
    while (3 * h + 1) < size // 3:
        h = h * 3 + 1
    h = max(h, 1)
    while h > 0:
        shell_method_engine(table, h)
        h = h // 3
    return table


def main():
    numer = input("Podaj jaki test chcesz wykonac: ")
    if numer == "1":
        #Test1
        List = [(5,'A'), (5,'B'), (7,'C'), (2,'D'), (5,'E'), (1,'F'), (7,'G'), (5,'H'), (1,'I'), (2,'J')]
        print(f'Orginał: {List}')
        table = [Elem(key, value) for key,value in  List]
        copy1 = table.copy()
        copy2 = table.copy()

        t_start = time.perf_counter()
        insertion_sorted = insertion_sort(table)
        t_stop = time.perf_counter()
        print(insertion_sorted)
        print("Czas obliczeń dla sortowania przez wstawianie:", "{:.7f}".format(t_stop - t_start))
        print("NIESTABILNE")

        t_start = time.perf_counter()
        shell_clasic_sorted = shell_method_classic(copy1)
        t_stop = time.perf_counter()
        print(shell_clasic_sorted)
        print("Czas obliczeń dla sortowania klasycznego shella:", "{:.7f}".format(t_stop - t_start))
        print("NIESTABILNE")

        t_start = time.perf_counter()
        shell_mod_sorted = shell_method_modified(copy2)
        t_stop = time.perf_counter()
        print(shell_mod_sorted)
        print("Czas obliczeń dla sortowania zmodyfikowanego shella:", "{:.7f}".format(t_stop - t_start))
        print("NIESTABILNE")

    if numer == "2":
        #Test2
        random_list = [random.randint(0, 99) for _ in range(10000)]
        copy1 = random_list.copy()
        copy2 = random_list.copy()
        copy3 = random_list.copy()
        
        t_start = time.perf_counter()
        insertion_sorted = insertion_sort(random_list)
        t_stop = time.perf_counter()
        print(insertion_sorted)
        print("Czas obliczeń dla sortowania przez wstawianie:", "{:.7f}".format(t_stop - t_start))

        t_start = time.perf_counter()
        shell_clasic_sorted = shell_method_classic(copy1)
        t_stop = time.perf_counter()
        print(shell_clasic_sorted)
        print("Czas obliczeń dla sortowania klasycznego shella:", "{:.7f}".format(t_stop - t_start))

        t_start = time.perf_counter()
        shell_mod_sorted = shell_method_modified(copy2)
        t_stop = time.perf_counter()
        print(shell_mod_sorted)
        print("Czas obliczeń dla sortowania zmodyfikowanego shella:", "{:.7f}".format(t_stop - t_start))

        heap = Queue(copy3)
        t_start = time.perf_counter()
        while not heap.is_empty():
            heap.dequeue()
        print(heap.table)
        t_stop = time.perf_counter()
        print("Czas obliczeń dla sortowania kopcowego:", "{:.7f}".format(t_stop - t_start))


if __name__ == "__main__":
    main()