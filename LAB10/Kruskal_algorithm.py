graf = [ ('A','B',4), ('A','C',1), ('A','D',4),
         ('B','E',9), ('B','F',9), ('B','G',7), ('B','C',5),
         ('C','G',9), ('C','D',3),
         ('D', 'G', 10), ('D', 'J', 18),
         ('E', 'I', 6), ('E', 'H', 4), ('E', 'F', 2),
         ('F', 'H', 2), ('F', 'G', 8),
         ('G', 'H', 9), ('G', 'J', 8),
         ('H', 'I', 3), ('H','J',9),
         ('I', 'J', 9)
        ]

class UnionFind:
    def __init__(self, n):
        self.p = [i for i in range(n)]
        self.size = [1 for _ in range(n)]

    def find(self, v):
        if self.p[v] == v:
            return v
        else:
            return self.find(self.p[v])
        
    def same_component(self, s1, s2):
        root1 = self.find(s1)
        root2 = self.find(s2)
        return root1 == root2

    def union_sets(self, s1, s2):
        root1 = self.find(s1)
        root2 = self.find(s2)
        if root1 == root2:
            return 
        elif self.size[root1] < self.size[root2]:
            self.p[root1] = root2
            self.size[root2] += self.size[root1]
        else:
            self.p[root2] = root1
            self.size[root1] += self.size[root2]

if __name__ == "__main__":
    #Prosty test
    union = UnionFind(6)
    union.union_sets(1,2)
    union.union_sets(4,5)
    print(f'Czy połączone 1-2: {union.same_component(1,2)}')
    print(f'Czy połączone 2-3: {union.same_component(2,3)}')
    print(f'Czy połączone 4-5: {union.same_component(4,5)}')

    print('_______________________________________')
    #Algorytm Kruskala
    graf.sort(key=lambda x: x[2])

    Union = UnionFind(len(graf))
    mst_res = []

    for s1, s2, weight in graf:
        s1_ascii = ord(s1) - ord('A')
        s2_ascii = ord(s2) - ord('A')

        if Union.same_component(s1_ascii, s2_ascii) is False:
            mst_res.append((s1, s2, weight))
            Union.union_sets(s1_ascii, s2_ascii)
    print(mst_res)
