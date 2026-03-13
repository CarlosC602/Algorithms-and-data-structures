from typing import List

class Linked_list:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def destroy(self):
        current_node = self.head 
        while current_node:
            next_node = current_node.next
            current_node.prev = None
            current_node.next =  None
            current_node = next_node
        self.head = None

    def add(self, data):
        new_node = Node(data)
        if self.is_empty() == True:
            self.head = new_node
            self.tail = new_node
            return
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node

    def append(self, data):
        new_node = Node(data)
        if self.is_empty() == True:
            self.head = new_node
            self.tail = new_node
            return
        new_node.prev = self.tail
        self.tail.next = new_node
        self.tail = new_node

    def remove(self):
        if self.is_empty() == True:
            return None
        if self.length() == 1:
            self.head = None
            self.tail = None
            return
        self.head = self.head.next
        self.head.prev = None

    def remove_end(self):
        if self.is_empty() == True:
            return None
        if self.length() == 1:
            self.head = None
            self.tail = None
            return
        self.tail = self.tail.prev
        self.tail.next = None

    def is_empty(self):
        return self.head is None
    
    def length(self):
        counter = 0
        current_node = self.head
        while current_node:
            counter += 1
            current_node = current_node.next
        return counter
    
    def get(self):
        if self.is_empty() == True:
            return None
        return self.head.data
    
    def display(self):
        current_node = self.head
        while current_node:
            print(f'-> {current_node.data}\n')
            current_node = current_node.next

    def displ_back(self):
        current_node = self.tail
        while current_node:
            print(f'-> {current_node.data}\n')
            current_node = current_node.prev


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

def main():
    List = [('AGH', 'Kraków', 1919),
            ('UJ', 'Kraków', 1364),
            ('PW', 'Warszawa', 1915),
            ('UW', 'Warszawa', 1915),
            ('UP', 'Poznań', 1919),
            ('PG', 'Gdańsk', 1945)]
    
    linked_list = Linked_list()

    for i in range(3):
        linked_list.append(List[i])

    for i in range(3,6):
        linked_list.add(List[i])

    linked_list.display()
    linked_list.displ_back()

    print(linked_list.length())

    linked_list.remove()

    print(linked_list.head.data)

    linked_list.remove_end()

    linked_list.display()
    linked_list.displ_back()

    #empty list
    linked_list.destroy()

    print(linked_list.is_empty())

    linked_list.remove()

    linked_list.remove_end()

    linked_list.append(List[0])

    linked_list.remove_end()

    print(linked_list.is_empty())


if __name__ == "__main__":
    main()