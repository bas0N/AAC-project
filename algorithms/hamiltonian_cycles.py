def find_hamiltonian_cycles(graph, is_directed):
    def is_valid_move(vertex, visited):
        # Check if vertex is not visited and there is an edge
        return not visited[vertex] and graph[path[-1]][vertex] == 1

    def backtrack(pos):
        # If all vertices are included and there is an edge back to the start
        if pos == n and graph[path[-1]][path[0]] == 1:
            cycles.append(path[:] + [path[0]])  # Add cycle to list
            return

        for next_vertex in range(n):
            if is_valid_move(next_vertex, visited):
                visited[next_vertex] = True
                path.append(next_vertex)
                backtrack(pos + 1)
                path.pop()
                visited[next_vertex] = False

    n = len(graph)
    cycles = []
    for start_vertex in range(n):
        visited = [False] * n
        path = [start_vertex]
        visited[start_vertex] = True
        backtrack(1)

    if not is_directed:
        # Remove duplicates for undirected graphs (rotations/reversals of cycles)
        unique_cycles = set(tuple(min(cycle[i:] + cycle[:i] for i in range(len(cycle)))) for cycle in cycles)
        cycles = [list(cycle) for cycle in unique_cycles]

    return len(cycles), cycles

