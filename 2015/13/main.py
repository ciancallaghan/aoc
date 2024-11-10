import itertools

class Graph:
    def __init__(self, graph: dict = {}):
        self.graph = graph

    def add_edge(self, node1, node2, weight):
        if node1 not in self.graph:
            self.graph[node1] = {}
        self.graph[node1][node2] = weight

def main():
    G = Graph()
    # with open("test_input.txt", "r") as f:
    with open("input.txt", "r") as f:
        for line in f.readlines():
            l = line.split()
            if "gain" in line:
                w = int(l[3])
            else:
                w = int(l[3]) * -1
            n1 = l[0]
            n2 = l[-1].strip(".")
            G.add_edge(n1, n2, w)

    perms = list(itertools.permutations(G.graph.keys()))
    h_diff = -10000
    for p in perms:
        diff = 0
        for i,g in enumerate(p):
            if i == len(p)-1:
                diff += G.graph[g][p[i-1]] + G.graph[g][p[0]]
            else:
                diff += G.graph[g][p[i-1]] + G.graph[g][p[i+1]]
        if diff >= h_diff:
            h_diff = diff
    print(h_diff)

    
    G1 = Graph(G.graph.copy())
    for k in G.graph.keys():
        G1.add_edge("Me", k, 0)
        G1.add_edge(k, "Me", 0)
    perms = list(itertools.permutations(G1.graph.keys()))
    h_diff = -10000
    for p in perms:
        diff = 0
        for i,g in enumerate(p):
            if i == len(p)-1:
                diff += G1.graph[g][p[i-1]] + G1.graph[g][p[0]]
            else:
                diff += G1.graph[g][p[i-1]] + G1.graph[g][p[i+1]]
        if diff >= h_diff:
            h_diff = diff
    print(h_diff)

main()
