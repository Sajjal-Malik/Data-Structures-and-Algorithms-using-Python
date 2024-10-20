class Graph:
    def __init__(self, vno):
        self.vertex_count = vno
        self.adj_list = {v:[] for v in range(vno)}

    def add_edge(self, u, v, weight=1):
        if self.vertex_count > u >= 0 and self.vertex_count > v >= 0:  # checking row and col indices
            self.adj_list[u].append((v, weight))
            self.adj_list[v].append((u, weight))
        else:
            print("Invalid vertex")
    
    def remove_edge(self, u, v):
        if self.vertex_count > u >= 0 and self.vertex_count > v >= 0:  # checking row and col indices
            self.adj_list[u] = [(vertex, weight) for vertex, weight in self.adj_list[u] if vertex != v]
            self.adj_list[v] = [(vertex, weight) for vertex, weight in self.adj_list[v] if vertex != u]
        else:
            print("Invalid vertex")
    
    def has_edge(self, u, v):
        if self.vertex_count > u >= 0 and self.vertex_count > v >= 0:  # checking row and col indices
            return any(vertex == v for vertex, x in self.adj_list[u])

    def print_adj_list(self):
        for vertex,n in self.adj_list.items():
            print("Vertex",vertex,":",n)


# driver code
g = Graph(5)
# g.add_edge(0, 0, 5)
# g.add_edge(0, 1, 10)
# g.add_edge(0, 2, 64)
# g.add_edge(0, 3, 50)
# g.add_edge(0, 4, 11)
# g.add_edge(1, 3, 55)
# g.add_edge(1, 4, 20)
# g.add_edge(2, 2, 40)
# g.add_edge(2, 3, 50)
# g.add_edge(3, 1, 35)
# g.add_edge(3, 2, 39)
# g.add_edge(4, 3, 25)
# g.add_edge(4, 4, 17)
g.add_edge(0, 0)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(0, 3)
g.add_edge(0, 4)
g.add_edge(1, 3)
g.add_edge(1, 4)
g.add_edge(2, 2)
g.add_edge(2, 3)
g.add_edge(3, 1)
g.add_edge(3, 2)
g.add_edge(4, 3)
g.add_edge(4, 4)
g.print_adj_list()
print()
g.remove_edge(0, 2)
g.remove_edge(2, 2)
g.print_adj_list()