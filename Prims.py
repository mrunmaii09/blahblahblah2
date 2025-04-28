def prims_mst(graph):
    start_node = list(graph.keys())[0]
    visited = set()
    edges = [(0, start_node)]
    total_cost = 0

    while edges:
        # Find the edge with the minimum cost manually
        edges.sort()
        cost, u = edges.pop(0)

        if u in visited:
            continue
        visited.add(u)
        total_cost += cost

        for v, weight in graph[u]:
            if v not in visited:
                edges.append((weight, v))

    return total_cost

# Example graph (undirected) as adjacency list
graph = {
    'A': [('B', 2), ('C', 3)],
    'B': [('A', 2), ('C', 1), ('D', 1)],
    'C': [('A', 3), ('B', 1), ('D', 4), ('E', 5)],
    'D': [('B', 1), ('C', 4), ('E', 2)],
    'E': [('C', 5), ('D', 2)]
}

print("Total cost of MST:", prims_mst(graph))
