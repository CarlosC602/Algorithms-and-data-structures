class Elem:
    def __init__(self, priority, data):
        self.__data = data
        self.__priority = priority

    def __lt__(self, other):
        return self.__priority < other.__priority
    
    def __gt__(self, other):
        return self.__priority > other.__priority
    
    def __repr__(self):
        return f"{self.__priority} : {self.__data}"

class Queue:
    def __init__(self):
        self.table = []
        self.size = 0

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
        self.table[0] = self.table[idx]
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

def main():
    queue = Queue()
    list = [7, 5, 1, 2, 5, 3, 4, 8, 9]
    list1 = "GRYMOTYLA"
    for priority, letter in zip(list, list1):
        elem = Elem(priority, letter)
        queue.enqueue(elem)
    queue.print_tree(0, 0)
    queue.print_tab()
    first_data = queue.dequeue()
    print(queue.peek())
    queue.print_tab()
    print(first_data)

    while queue.size > 0:
        deleted_data = queue.dequeue()
        print(deleted_data)
    queue.print_tab()

if __name__ == "__main__":
    main()

    
