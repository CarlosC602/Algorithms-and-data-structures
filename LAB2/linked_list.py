from typing import List

class Linked_list:
    def __init__(self):
        self.head = None
    
    def destroy(self):
        self.head = None

    def add(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def append(self, data):
        node_to_add = Node(data)
        if self.is_empty() == True:
            return node_to_add
        
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = node_to_add

    def remove(self):
        if self.is_empty() != True:
            self.head = self.head.next

    def remove_end(self):
        if self.is_empty() == True:
            return None
        
        if self.length() == 1:
            self.head = None
            return None
        
        current_node = self.head
        while current_node.next.next:
            current_node = current_node.next
        current_node.next = None

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

            

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

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

    print(linked_list.length())

    linked_list.remove()

    print(linked_list.head)

    linked_list.remove_end()

    linked_list.display()

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