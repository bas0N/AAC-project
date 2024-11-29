import random

def normalize_cycle(path, is_directed):
    edges = []
    for i in range(len(path)):
        u, v = path[i], path[(i + 1) % len(path)]
        edges.append((u, v))

    if is_directed:
        # For directed graphs, normalize by finding the lexicographically smallest rotation of edges
        min_rotation = edges[:]
        for i in range(1, len(edges)):
            rotation = edges[i:] + edges[:i]
            if rotation < min_rotation:
                min_rotation = rotation
        normalized = min_rotation
    else:
        # For Undirected graphs, handle all rotations and reversed rotations
        edges = [tuple(sorted(edge)) for edge in edges]  # Sort vertices inside each edge
        # Generate all rotations of the cycle
        all_rotations = []
        n = len(edges)

        for i in range(n):
            rotation = edges[i:] + edges[:i]
            all_rotations.append(rotation)
            # Also consider the reversed cycle (since undirected graph doesn't care about direction)
            all_rotations.append(rotation[::-1])

        # Sort all rotations lexicographically and pick the smallest one
        canonical_cycle = min(all_rotations)
        normalized = tuple(canonical_cycle)

    return normalized

def find_all_cycles(input_data):
    graph, is_directed = input_data["adjacency_matrix"], input_data["is_directed"]
    def dfs(v, start, visited, path, cycles):
        visited[v] = True
        path.append(v)

        for neighbor in range(len(graph)):
            # If there's an edge and it's either a directed graph or the neighbor hasn't been visited
            if graph[v][neighbor] > 0:
                if not visited[neighbor]:
                    dfs(neighbor, start, visited, path, cycles)
                elif neighbor == start and len(path) > 2:  # A cycle is detected
                    normalized = normalize_cycle(path, is_directed)

                    if normalized not in cycles:
                        cycles.append(normalized)

        path.pop()
        visited[v] = False

    all_cycles = []
    for start_vertex in range(len(graph)):
        visited = [False] * len(graph)
        dfs(start_vertex, start_vertex, visited, [], all_cycles)

    # Find the maximum cycle size and count the cycles with that size
    max_cycle_length = max(len(cycle) for cycle in all_cycles) if all_cycles else 0
    max_cycles = [cycle for cycle in all_cycles if len(cycle) == max_cycle_length]

    return {"cycles": all_cycles, "max_cycle_length": max_cycle_length, "max_cycles": max_cycles}

def approximate_max_cycles(input_data):
    adj_matrix, iterations, is_directed = input_data["adjacency_matrix"], input_data["iterations"], input_data["is_directed"]
    """
    Approximate the maximum cycle length and count the number of such cycles in a graph.

    Args:
        adj_matrix (list[list[int]]): Adjacency matrix of the graph.
        iterations (int): Number of random walks to perform.
        is_directed (bool): Whether the graph is directed or undirected.

    Returns:
        tuple: (max_cycle_length, number_of_max_cycles)
    """
    n = len(adj_matrix)

    def greedy_longest_cycle():
        """Greedy algorithm to find an approximate longest cycle, with randomness."""
        visited = [False] * n
        cycle = []

        def find_next_node(current_node):
            """Find the next best node to extend the cycle, introducing randomness."""
            candidates = []
            for neighbor in range(n):
                if adj_matrix[current_node][neighbor] == 1 and not visited[neighbor]:
                    candidates.append(neighbor)

            if not candidates:
                return None

            return random.choice(candidates)

        # Start from a random node
        start_node = random.randint(0, n - 1)
        cycle.append(start_node)
        visited[start_node] = True
        current_node = start_node

        while True:
            next_node = find_next_node(current_node)
            if next_node is None:
                # Try to close the cycle
                if adj_matrix[current_node][start_node] == 1:
                    return cycle
                break
            cycle.append(next_node)
            visited[next_node] = True
            current_node = next_node

        return cycle

    # Step 1: Perform multiple iterations to gather cycles
    normalized_cycles = set()

    for _ in range(iterations):
        cycle = greedy_longest_cycle()
        if cycle:
            normalized_cycle = normalize_cycle(cycle, is_directed)
            normalized_cycles.add(tuple(normalized_cycle))

    # Step 2: Ensure non-empty list of cycles
    if not normalized_cycles:
        return 0, 0

    # Step 3: Find the maximum cycle length
    max_cycle_length = max(len(cycle) for cycle in normalized_cycles)

    # Step 4: Filter out the maximum length cycles
    max_cycles = [cycle for cycle in normalized_cycles if len(cycle) == max_cycle_length]
    return {"max_cycles_length_approx":max_cycle_length, "num_max_cycles_approx": len(max_cycles)}
