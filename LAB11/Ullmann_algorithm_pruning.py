import copy

class Matrix:
    def __init__(self, arg, val = 0):
        self.__matrix = []
        if isinstance(arg, tuple):
            rows, cols = arg
            for _ in range(rows):
                row_ = []
                for _ in range(cols):
                    row_.append(val)
                self.__matrix.append(row_)
        else:
            for row in arg:
                row_ = []
                for value in row:
                    row_.append(value)
                self.__matrix.append(row_)
    
    def size(self):
        rows = len(self.__matrix)
        cols = len(self.__matrix[0]) if rows > 0 else 0
        return rows, cols
    
    def __getitem__(self, index):
        return self.__matrix[index]
    
    def __add__(self, other):
        r1, c1 = self.size()
        r2, c2 = other.size()
        if (r1, c1) != (r2, c2):
            return None
        
        result = Matrix((r1, c1))

        for i in range(r1):
            for j in range(c1):
                result[i][j] = self[i][j] + other[i][j]
        return result
    
    def __mul__(self, other):
        r1, c1 = self.size()
        r2, c2 = other.size()

        if c1 != r2:
            return None
        
        result = Matrix((r1,c2))

        for i in range(r1):
            for j in range(c2):
                suma = 0
                for k in range(c1):
                    suma += self[i][k] * other[k][j]
                result[i][j] = suma
        return result
    
    def __eq__(self, other):
        if not isinstance(other, Matrix):
            return False

        if self.size() != other.size():
            return False
        
        r,c = self.size()

        for i in range(r):
            for j in range(c):
                if self[i][j] != other[i][j]:
                    return False
        return True
    
    def __str__(self):
        result = ""
        for row in self.__matrix:
            result += "| "
            for elem in row:
                result += str(elem) + " "
            result += "|\n"
        return result
                
def transpose(matrix: Matrix):
    r,c = matrix.size()
    res = Matrix((c,r))
    for i in range(r):
        for j in range(c):
            res[j][i] = matrix[i][j]
    return res



class matrix_graph:
    def __init__(self, default_edge=0):
        self.vertex_list = []
        self.matrix = Matrix((0,0), val=default_edge)
        self.default_edge = default_edge

    def is_empty(self):
        if len(self.vertex_list) == 0:
            return True
        
    def insert_vertex(self, vertex):
        if vertex in self.vertex_list:
            return
        self.vertex_list.append(vertex)

        old_size = self.matrix.size()[0]
        new_size = old_size + 1
        new_matrix = Matrix((new_size, new_size), val=self.default_edge)

        for i in range(old_size):
            for j in range(old_size):
                new_matrix[i][j] = self.matrix[i][j]
        self.matrix = new_matrix

    def insert_edge(self, vertex1, vertex2, edge=1):
        idx1 = self.vertex_list.index(vertex1)
        idx2 = self.vertex_list.index(vertex2)

        self.matrix[idx1][idx2] = edge
        self.matrix[idx2][idx1] = edge

    def delete_vertex(self, vertex):
        idx = self.vertex_list.index(vertex)
        self.vertex_list.pop(idx)
        
        old_size = self.matrix.size()[0]
        new_size = old_size - 1

        new_matrix = Matrix((new_size, new_size), val=self.default_edge)
        
        for i in range(old_size):
            if i == idx:
                continue
            new_i = i if i < idx else i - 1
            
            for j in range(old_size):
                if j == idx:
                    continue
                new_j = j if j < idx else j - 1
                
                new_matrix[new_i][new_j] = self.matrix[i][j]
                
        self.matrix = new_matrix

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


def build_graph(edge_list):
    g = matrix_graph(default_edge=0)
    vertices = set()
    for v1, v2, _ in edge_list:
        vertices.add(v1)
        vertices.add(v2)

    for v in sorted(list(vertices)):
        g.insert_vertex(v)

    for v1, v2, weight in edge_list:
        g.insert_edge(v1, v2, weight)  
    return g

            
def get_degrees(graph_obj):
    degrees = []
    rows, cols = graph_obj.matrix.size()
    for i in range(rows):
        deg = sum(graph_obj.matrix[i][j] for j in range(cols) if graph_obj.matrix[i][j] > 0)
        degrees.append(deg)
    return degrees

def create_M0(G, P):
    deg_G = get_degrees(G)
    deg_P = get_degrees(P)
    
    p_rows = P.matrix.size()[0]
    g_cols = G.matrix.size()[0]
    
    M0 = Matrix((p_rows, g_cols), val=0)
    
    for i in range(p_rows):
        for j in range(g_cols):
            if deg_P[i] <= deg_G[j]:
                M0[i][j] = 1
    return M0


def prune(M, G, P):
    changed = True
    while changed:
        changed = False
        p_rows, g_cols = M.size()
        for i in range(p_rows):
            for j in range(g_cols):
                if M[i][j] == 1:
                    for x in range(p_rows):
                        if P[i][x] > 0:
                            match_found = False
                            for y in range(g_cols):
                                if G[j][y] > 0 and M[x][y] == 1:
                                    match_found = True
                                    break
                            if not match_found:
                                M[i][j] = 0
                                changed = True
                                break


def Ullmann_v3(cols, idx, M, G, P):
    isomorphisms = 0
    calls = 1 
    rows, num_cols = M.size()

    if idx == rows:
        MG_T = transpose(M * G)
        if P == M * MG_T:
            return 1, calls
        return 0, calls
    M_copy = copy.deepcopy(M)
    prune(M_copy, G, P)
    for col in range(num_cols):
        if not cols[col] and M_copy[idx][col] == 1:
            M_next = copy.deepcopy(M_copy)
            cols[col] = True
            for i in range(num_cols):
                M_next[idx][i] = 0
            M_next[idx][col] = 1
            sub_iso, sub_calls = Ullmann_v3(cols, idx + 1, M_next, G, P)
            isomorphisms += sub_iso
            calls += sub_calls
            cols[col] = False

    return isomorphisms, calls


if __name__ == '__main__':
    graph_G = [ ('A','B',1), ('B','F',1), ('B','C',1), ('C','D',1), ('C','E',1), ('D','E',1)]
    graph_P = [ ('A','B',1), ('B','C',1), ('A','C',1)]

    G = build_graph(graph_G)
    P = build_graph(graph_P)

    p_rows = P.matrix.size()[0]
    g_cols = G.matrix.size()[0]

    M_start_v3 = create_M0(G, P)
    cols_used_v3 = [False] * g_cols
    iso_v3, calls_v3 = Ullmann_v3(cols_used_v3, 0, M_start_v3, G.matrix, P.matrix)

    print(f"{iso_v3} {calls_v3}")