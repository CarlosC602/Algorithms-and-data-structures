import polska

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
    

class matrix_graph:
    def __init__(self, default_edge=0):
        self.vertex_list = []
        self.matrix = []
        self.default_edge = default_edge

    def is_empty(self):
        if len(self.vertex_list) == 0:
            return True
        
    def insert_vertex(self, vertex):
        if vertex in self.vertex_list:
            return
        self.vertex_list.append(vertex)
        for row in self.matrix:
            row.append(self.default_edge)
        new_row = [self.default_edge] * len(self.vertex_list)
        self.matrix.append(new_row)

    def insert_edge(self, vertex1, vertex2, edge=1):
        idx1 = self.vertex_list.index(vertex1)
        idx2 = self.vertex_list.index(vertex2)

        self.matrix[idx1][idx2] = edge
        self.matrix[idx2][idx1] = edge

    def delete_vertex(self, vertex):
        idx = self.vertex_list.index(vertex)
        self.vertex_list.pop(idx)
        self.matrix.pop(idx)
        for row in self.matrix:
            row.pop(idx)    

    def delete_edge(self, vertex1, vertex2):
        idx1 = self.vertex_list.index(vertex1)
        idx2 = self.vertex_list.index(vertex2)

        self.matrix[idx1][idx2] = self.default_edge
        self.matrix[idx2][idx1] = self.default_edge

    def get_vertex(self, vertex_id):
        return self.vertex_list[vertex_id]
    
    def vertices(self):
        for i in range(len(self.vertex_list)):
            yield i

    def neighbours(self, vertex_id):
        for i, edge_val in enumerate(self.matrix[vertex_id]):
            if edge_val != self.default_edge:
                yield (i, edge_val)
  

def test_graph(graph):
    for key1, key2 in polska.graf:
        v1 = Vertex(key1)
        v2 = Vertex(key2)

        graph.insert_vertex(v1)
        graph.insert_vertex(v2)
        
        graph.insert_edge(v1, v2)

    malopolskie = Vertex('K')
    graph.delete_vertex(malopolskie)

    mazowieckie = Vertex('W')
    lodzkie = Vertex('E')
    graph.delete_edge(mazowieckie, lodzkie)

    polska.draw_map(graph)


if __name__ == "__main__":
    print("Testowanie Listy Sąsiedztwa...")
    graf_lista = list_graph()
    test_graph(graf_lista)
    
    print("Testowanie Macierzy Sąsiedztwa...")
    graf_macierz = matrix_graph()
    test_graph(graf_macierz)