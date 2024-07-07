def dijkstra(graph, root):
    distances = {node: float('infinity') for node in graph}
    distances[root] = 0

    to_visit = set(graph.keys())

    while to_visit:
        current_node = None

        for node in to_visit:
            if current_node is None or distances[node] < distances[current_node]:
                current_node = node

        if distances[current_node] == float('infinity'):
            break

        for neighbor, weight in graph[current_node]:
            temp_distance = distances[current_node] + weight

            if temp_distance < distances[neighbor]:
                distances[neighbor] = temp_distance

        to_visit.remove(current_node)

    return distances

graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 2), ('D', 5)],
    'C': [('A', 4), ('B', 2), ('D', 1)],
    'D': [('B', 5), ('C', 1)]
}

# Running the algorithm
print(dijkstra(graph, 'A'))

