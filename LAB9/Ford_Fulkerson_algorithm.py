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
    
class Edge:
    def __init__(self, capacity, r):
        self.capacity = capacity
        self.r = r
        if r is not True:
            self.capacity_r = capacity
            self.flow = 0
        else:
            self.capacity_r = 0
            self.flow = 0
    
    def __repr__(self):
        return f"({self.capacity} {self.flow} {self.capacity_r} {self.r})"
    
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

    def get_vertex(self, vertex_id):
        return vertex_id
    
    def vertices(self):
        return self.graph.keys()
    
    def neighbours(self, vertex_id):
        return self.graph[vertex_id].items()
    
    def get_edge(self, vertex1_id, vertex2_id):
        return self.graph[vertex1_id][vertex2_id]
    
def build_graph(edge_list):
    g = list_graph()
    for v1, v2, capacity in edge_list:
        g.insert_vertex(v1)
        g.insert_vertex(v2)

        real_edge = Edge(capacity, False)
        g.insert_edge(v1, v2, real_edge)

        residual_edge = Edge(0, True)
        g.insert_edge(v2, v1, residual_edge)
    return g

def printGraph(g):
    print("------GRAPH------")
    for v in g.vertices():
        print(v, end = " -> ")
        for (n, w) in g.neighbours(v):
            print(n, w, end=";")
        print()
    print("-------------------")

def BFS(graph, start_vertex, end_vertex):
    visited = set()
    parent = {}
    queue = []

    queue.append(start_vertex)
    visited.add(start_vertex)

    while len(queue) > 0:
        curr_vert = queue.pop(0)

        if curr_vert == end_vertex:
            break

        for neighbour, edge in graph.neighbours(curr_vert):
            if neighbour not in visited and edge.capacity_r > 0:
                queue.append(neighbour)
                visited.add(neighbour)
                parent[neighbour] = curr_vert

    return parent

def minimal_capacity(graph, start_vertex, end_vertex, parent):
    if end_vertex not in parent:
        return 0
    min_capacity = float('inf')
    current_vertex = end_vertex
    
    while current_vertex is not start_vertex:
        p = parent[current_vertex]
        curr_edge = graph.get_edge(p, current_vertex)
        if curr_edge.capacity_r < min_capacity:
            min_capacity = curr_edge.capacity_r
        current_vertex = p
    return min_capacity

def path_augmentation(graph, start_vertex, end_vertex, parent, min_capacity):
    current_vertex = end_vertex
    
    while current_vertex is not start_vertex:
        p = parent[current_vertex]
        p_curr_ver = graph.get_edge(p, current_vertex)
        curr_ver_p = graph.get_edge(current_vertex, p)

        p_curr_ver.capacity_r -= min_capacity
        curr_ver_p.capacity_r += min_capacity
        current_vertex = p

        if not p_curr_ver.r:
            p_curr_ver.flow += min_capacity
        else:
            curr_ver_p.flow -= min_capacity

def Edmonds_Karp_algorithm(graph, start_vertex, end_vertex):
    while True:
        parent = BFS(graph, start_vertex, end_vertex)
        new_flow = minimal_capacity(graph, start_vertex, end_vertex, parent)
        if new_flow == 0:
            break
        path_augmentation(graph, start_vertex, end_vertex, parent, new_flow)

    total_flow = 0

    for v in graph.vertices():
        if end_vertex in graph.graph[v]:
            edge = graph.get_edge(v, end_vertex)
            if not edge.r:
                total_flow += edge.flow    
    return total_flow

def get_outgoing_flow(graph, vertex_id):
    out_flow = 0
    for neighbour, edge in graph.neighbours(vertex_id):
        if not edge.r:
            out_flow += edge.flow
    return out_flow

if __name__ == '__main__':
    
    print("=== TEST 0 ===")
    graf_0 = [ ('s','u',2), ('u','t',1), ('u','v',3), ('s','v',1), ('v','t',2)]
    g0 = build_graph(graf_0)
    print(Edmonds_Karp_algorithm(g0, 's', 't')) 
    printGraph(g0)
    print("Przepływ wypływający z węzła 'u':", get_outgoing_flow(g0, 'u'))
    print("\n")


    print("=== TEST 1 ===")
    graf_1 = [ ('s', 'a', 16), ('s', 'c', 13), ('a', 'c', 10), ('a', 'b', 12), ('b', 'c', 9), ('b', 't', 20), ('c', 'd', 14), ('d', 'b', 7), ('d', 't', 4) ]
    g1 = build_graph(graf_1)
    print(Edmonds_Karp_algorithm(g1, 's', 't')) 
    printGraph(g1)
    print("Przepływ wypływający z węzła 'a':", get_outgoing_flow(g1, 'a'))
    print("\n")


    print("=== TEST 2 ===")
    graf_2 = [ ('s', 'a', 3), ('s', 'c', 3), ('a', 'b', 4), ('b', 's', 3), ('b', 'c', 1), ('b', 'd', 2), ('c', 'e', 6), ('c', 'd', 2), ('d', 't', 1), ('e', 't', 9)]
    g2 = build_graph(graf_2)
    print(Edmonds_Karp_algorithm(g2, 's', 't')) 
    printGraph(g2)
    print("Przepływ wypływający z węzła 'a':", get_outgoing_flow(g2, 'a'))
    print("\n")


    print("=== TEST 3 ===")
    graf_3 = [('s', 'a', 3), ('s', 'd', 2), ('a', 'b', 4), ('b', 'c', 5), ('c', 't', 6), ('a', 'f', 3),  ('f', 't', 3), ('d', 'e', 2), ('e','f',2)]
    g3 = build_graph(graf_3)
    print(Edmonds_Karp_algorithm(g3, 's', 't')) 
    printGraph(g3)
    print("Przepływ wypływający z węzła 'a':", get_outgoing_flow(g3, 'a'))