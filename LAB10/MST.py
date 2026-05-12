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

class Vertex:
    def __init__(self, key):
        self.key = key

    def __hash__(self):
        return hash(self.key)
    
    def __eq__(self, other):
        if self.key == other.key:
            return True
        else:
            return False
    
    def __repr__(self):
        return str(self.key)
    
class list_graph:
    def __init__(self):
        self.graph = {}

    def is_empty(self):
        if len(self.graph) == 0:
            return True
    
    def insert_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = {}

    def insert_edge(self, vertex1, vertex2, edge=None):
        self.graph[vertex1][vertex2] = edge
        self.graph[vertex2][vertex1] = edge

    def delete_vertex(self, vertex):
        if vertex not in self.graph:
            return
        for neighbour in self.graph[vertex]:
            del self.graph[neighbour][vertex]
        del self.graph[vertex]

    def delete_edge(self, vertex1, vertex2):
        if vertex1 not in self.graph or vertex2 not in self.graph:
            return
        del self.graph[vertex1][vertex2]
        del self.graph[vertex2][vertex1]

    def get_vertex(self, vertex_id):
        return vertex_id
    
    def vertices(self):
        return self.graph.keys()
    
    def neighbours(self, vertex_id):
        return self.graph[vertex_id].items()

def printGraph(g):
    print("------GRAPH------")
    for v in g.vertices():
        print(v, end = " -> ")
        for (n, w) in g.neighbours(v):
            print(n, w, end=";")
        print()
    print("-------------------")
  
def Prim_algorithm(g):
    intree = {v: False for v in g.vertices()}
    weight = {v: float('inf') for v in g.vertices()}
    parent = {v: None for v in g.vertices()}

    mst = list_graph()
    for v in g.vertices():
        mst.insert_vertex(v)

    start_node = list(g.vertices())[0]
    weight[start_node] = 0
    total_weight = 0

    while True:
        u = None
        min_w = float('inf')
        for v in g.vertices():
            if not intree[v] and weight[v] < min_w:
                min_w = weight[v]
                u = v
        if u is None:
            break

        intree[u] = True
        if parent[u] is not None:
            mst.insert_edge(u, parent[u], weight[u])
            total_weight += weight[u]

        neighbours = g.neighbours(u)
        for n, val in neighbours:
            if intree[n] == False and weight[n] > val:
                weight[n] = val
                parent[n] = u
    return mst, total_weight


if __name__ == "__main__":
    graph1 = list_graph()
    for w1, w2, weight in graf:
        graph1.insert_vertex(w1)
        graph1.insert_vertex(w2)
        graph1.insert_edge(w1, w2, weight)

    mst, _ = Prim_algorithm(graph1)

    printGraph(mst)