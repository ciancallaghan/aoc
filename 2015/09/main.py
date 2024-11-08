import itertools

class Graph:
    def __init__(self, graph: dict = {}):
        self.graph = graph

    def add_edge(self, node1, node2, weight):
        if node1 not in self.graph:
            self.graph[node1] = {}
        if node2 not in self.graph:
            self.graph[node2] = {}
        self.graph[node1][node2] = int(weight)
        self.graph[node2][node1] = int(weight)
       

def main():
    min_dist = 10000
    max_dist = 0

    G = Graph()
    with open("input.txt", "r") as f:
        for line in f.readlines():
            line = line.split()
            line[-1] = int(line[-1])
            G.add_edge(line[0], line[2], line[-1])

    perms = list(itertools.permutations(G.graph.keys()))

    for p in perms:
        dist = 0
        for i in range(len(p) - 1):
            dist += G.graph[p[i]][p[i+1]]
        if dist < min_dist:
            min_dist = dist
        if dist > max_dist:
            max_dist = dist
    print(min_dist)
    print(max_dist)
    
main()
