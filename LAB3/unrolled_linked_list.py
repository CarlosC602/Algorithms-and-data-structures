Max_Node_Size = 6
class Node:
    def __init__(self):
        self.tab = [None for _ in range(Max_Node_Size)]
        self.next = None
        self.counter = 0

    def add_value(self, val, idx):
        i = self.counter
        while i != idx:
            self.tab[i] = self.tab[i-1]
            i -= 1
        self.tab[idx] = val
        self.counter += 1

    def delete_value(self, idx):
        for i in range(idx, self.counter - 1):
            self.tab[i] = self.tab[i + 1]
        self.tab[self.counter - 1] = None
        self.counter -= 1


class unroleld_linked_list:
    def __init__(self):
        self.head = Node()
        self.total_elems = 0

    def get(self, idx):
        curr = self.head
        while curr is not None and idx >= curr.counter:
            idx -= curr.counter
            curr = curr.next
        if curr is not None:
                return curr.tab[idx]
        return None
    
    def insert(self, data, idx):
        if idx > self.total_elems:
            idx = self.total_elems
        elif idx < 0:
            idx = 0
        
        curr = self.head
        while curr.next is not None and idx >= curr.counter:       
            idx -= curr.counter
            curr = curr.next

        if idx > curr.counter:
            idx = curr.counter

        if curr.counter == Max_Node_Size:
            new_node = Node()
            half = Max_Node_Size // 2
            move_count = Max_Node_Size - half

            for i in range(move_count):
                new_node.tab[i] = curr.tab[half + i]
                curr.tab[half + i] = None
            
            new_node.counter = move_count
            curr.counter = half

            new_node.next = curr.next
            curr.next = new_node

            if idx <= curr.counter:
                curr.add_value(data, idx)

            else:
                new_node.add_value(data, idx - curr.counter)
        else:
            curr.add_value(data, idx)

        self.total_elems += 1

    def delete(self, idx):
        curr = self.head
        while curr is not None and idx >= curr.counter:
            idx -= curr.counter
            curr = curr.next
        
        curr.tab[idx] = None

        for i in range(idx, curr.counter - 1):
            curr.tab[i] = curr.tab[i + 1]

        curr.tab[curr.counter - 1] = None
        curr.counter -= 1

        half = Max_Node_Size // 2
        if curr.counter < half and curr.next is not None:
            move_count = half - curr.counter + 1
            move_count = min(move_count, curr.next.counter)

            for i in range (move_count):
                curr.tab[curr.counter] = curr.next.tab[0]
                curr.counter += 1

                for j in range(curr.next.counter -1):
                    curr.next.tab[j] = curr.next.tab[j + 1]

                curr.next.tab[curr.next.counter - 1] = None
                curr.next.counter -= 1

            if curr.next.counter < half:
                while curr.next.counter > 0:
                    curr.tab[curr.counter] = curr.next.tab[0]
                    curr.counter += 1

                    for j in range(curr.next.counter - 1):
                        curr.next.tab[j] = curr.next.tab[j + 1]
                    curr.next.counter -= 1
                curr.next = curr.next.next
        self.total_elems -= 1

    def print_list(self):
        current = self.head
        idx = 0
        while current is not None:
            print(f"Węzeł [{idx}]: {current.tab[:current.counter]}")
            current = current.next
            idx += 1
    

def main():
    List = unroleld_linked_list()
    for i in range(9):
        List.insert(i+1,i)

    print(List.get(4))
    List.insert(10,1)
    List.insert(11,8)
    List.print_list()
    List.delete(1)
    List.delete(2)
    List.print_list()

if __name__ == "__main__":
    main()