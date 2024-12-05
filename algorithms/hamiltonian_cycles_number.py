# find all hamiltonian cycles (backtracking - exact solution)
def count_hamiltonian_cycles_bac(adj_matrix, is_directed):
    """
    Counts the number of Hamiltonian cycles in a graph using a backtracking approach.

    Args:
        adj_matrix (list[list[int]]): Adjacency matrix of the graph.
        is_directed (bool): True if the graph is directed, False otherwise.

    Returns:
        int: The number of Hamiltonian cycles.
    """
    def backtrack(path):
        nonlocal cycle_count

        # If we've visited all nodes, check if we can form a cycle back to the start
        if len(path) == n:
            if adj_matrix[path[-1]][path[0]] == 1:
                cycle = normalize_cycle(path + [path[0]], is_directed)
                if cycle not in unique_cycles:
                    unique_cycles.add(cycle)
                    cycle_count += 1
            return

        for next_node in range(n):
            if next_node not in visited and adj_matrix[path[-1]][next_node] == 1:
                # Add the node to the path and mark it as visited
                visited.add(next_node)
                path.append(next_node)

                # Recur to explore further
                backtrack(path)

                # Backtrack
                path.pop()
                visited.remove(next_node)

    # Helper function: Normalize cycle
    def normalize_cycle(path, is_directed):
        edges = []
        for i in range(len(path) - 1):
            u, v = path[i], path[i + 1]
            edges.append((u, v))

        if is_directed:
            # For directed graphs, normalize by finding the lexicographically smallest rotation of edges
            min_rotation = edges[:]
            for i in range(1, len(edges)):
                rotation = edges[i:] + edges[:i]
                if rotation < min_rotation:
                    min_rotation = rotation
            normalized = tuple(min_rotation)
        else:
            # For undirected graphs, handle all rotations and reversed rotations
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

    n = len(adj_matrix)
    unique_cycles = set()
    visited = set()
    cycle_count = 0

    # Start backtracking from each node
    for start_node in range(n):
        visited.add(start_node)
        backtrack([start_node])
        visited.remove(start_node)

    return cycle_count



# find all hamiltonian cycles (approximation - random solution)
import random

def count_hamiltonian_cycles_randomized(adj_matrix, is_directed, iterations=1000):
    """
    Counts the number of Hamiltonian cycles in a graph using a randomized approach.

    Args:
        adj_matrix (list[list[int]]): Adjacency matrix of the graph.
        is_directed (bool): True if the graph is directed, False otherwise.
        iterations (int): Number of random paths to evaluate.

    Returns:
        int: The estimated number of Hamiltonian cycles.
    """
    def is_valid_cycle(path):
        """Check if the path is a valid Hamiltonian cycle."""
        for i in range(len(path)):
            u, v = path[i], path[(i + 1) % len(path)]
            if adj_matrix[u][v] == 0:
                return False
        return True

    def normalize_cycle(path, is_directed):
        """Normalize cycle for uniqueness."""
        edges = [(path[i], path[(i + 1) % len(path)]) for i in range(len(path))]

        if is_directed:
            # Lexicographically smallest rotation for directed graphs
            min_rotation = edges[:]
            for i in range(1, len(edges)):
                rotation = edges[i:] + edges[:i]
                if rotation < min_rotation:
                    min_rotation = rotation
            return tuple(min_rotation)
        else:
            # Handle undirected case: consider all rotations and reversals
            edges = [tuple(sorted(edge)) for edge in edges]
            all_rotations = []
            for i in range(len(edges)):
                rotation = edges[i:] + edges[:i]
                all_rotations.append(rotation)
                all_rotations.append(rotation[::-1])
            return tuple(min(all_rotations))

    n = len(adj_matrix)
    nodes = list(range(n))
    unique_cycles = set()

    for _ in range(iterations):
        # Randomly shuffle the nodes to create a random path
        random.shuffle(nodes)
        if is_valid_cycle(nodes):
            # Normalize the cycle and add it to the set of unique cycles
            normalized_cycle = normalize_cycle(nodes, is_directed)
            unique_cycles.add(normalized_cycle)

    return len(unique_cycles)

# find all hamiltonian cycles (approximation - biased solution)
import random
from collections import defaultdict

def count_hamiltonian_cycles_biased(adj_matrix, is_directed, iterations=1000):
    """
    Counts the number of Hamiltonian cycles in a graph using a biased randomized approach.

    Args:
        adj_matrix (list[list[int]]): Adjacency matrix of the graph.
        is_directed (bool): True if the graph is directed, False otherwise.
        iterations (int): Number of random paths to evaluate.

    Returns:
        int: The estimated number of Hamiltonian cycles.
    """
    def is_valid_cycle(path):
        """Check if the path is a valid Hamiltonian cycle."""
        for i in range(len(path)):
            u, v = path[i], path[(i + 1) % len(path)]
            if adj_matrix[u][v] == 0:
                return False
        return True

    def normalize_cycle(path, is_directed):
        """Normalize cycle for uniqueness."""
        edges = [(path[i], path[(i + 1) % len(path)]) for i in range(len(path))]

        if is_directed:
            # Lexicographically smallest rotation for directed graphs
            min_rotation = edges[:]
            for i in range(1, len(edges)):
                rotation = edges[i:] + edges[:i]
                if rotation < min_rotation:
                    min_rotation = rotation
            return tuple(min_rotation)
        else:
            # Handle undirected case: consider all rotations and reversals
            edges = [tuple(sorted(edge)) for edge in edges]
            all_rotations = []
            for i in range(len(edges)):
                rotation = edges[i:] + edges[:i]
                all_rotations.append(rotation)
                all_rotations.append(rotation[::-1])
            return tuple(min(all_rotations))

    def calculate_degrees(adj_matrix):
        """Calculate the degree of each node."""
        return [sum(row) for row in adj_matrix]

    n = len(adj_matrix)
    degrees = calculate_degrees(adj_matrix)
    nodes = list(range(n))
    unique_cycles = set()

    # Identify bridge nodes (nodes with minimum degree)
    min_degree = min(degrees)
    bridge_nodes = [i for i, d in enumerate(degrees) if d == min_degree]

    for _ in range(iterations):
        # Start with a priority queue: high-degree nodes first, bridge nodes early
        nodes.sort(key=lambda x: (-degrees[x], x))  # High degree first, ties broken by node index
        path = []

        # Randomly prioritize bridge nodes at the beginning
        if bridge_nodes and random.random() < 0.5:
            start_node = random.choice(bridge_nodes)
            path.append(start_node)
            remaining_nodes = [node for node in nodes if node != start_node]
        else:
            remaining_nodes = nodes[:]

        # Construct a random Hamiltonian path with bias
        while remaining_nodes:
            next_node = random.choice(remaining_nodes)
            path.append(next_node)
            remaining_nodes.remove(next_node)

        if is_valid_cycle(path):
            # Normalize the cycle and add it to the set of unique cycles
            normalized_cycle = normalize_cycle(path, is_directed)
            unique_cycles.add(normalized_cycle)

    return len(unique_cycles)


# find all hamiltonian cycles (approximation - genetic solution)
import random

def count_hamiltonian_cycles_genetic(adj_matrix, is_directed, iterations=1000, population_size=50, generations=100):
    def is_valid_cycle(path):
        """Check if the path is a valid Hamiltonian cycle."""
        for i in range(len(path)):
            u, v = path[i], path[(i + 1) % len(path)]
            if adj_matrix[u][v] == 0:
                return False
        return True

    def normalize_cycle(path, is_directed):
        """Normalize cycle for uniqueness."""
        edges = [(path[i], path[(i + 1) % len(path)]) for i in range(len(path))]
        if is_directed:
            min_rotation = edges[:]
            for i in range(1, len(edges)):
                rotation = edges[i:] + edges[:i]
                if rotation < min_rotation:
                    min_rotation = rotation
            return tuple(min_rotation)
        else:
            edges = [tuple(sorted(edge)) for edge in edges]
            all_rotations = []
            for i in range(len(edges)):
                rotation = edges[i:] + edges[:i]
                all_rotations.append(rotation)
                all_rotations.append(rotation[::-1])
            return tuple(min(all_rotations))

    def cycle_from_normalized(normalized_cycle):
        """Convert a normalized cycle (tuple of edges) back to a list of nodes."""
        return [edge[0] for edge in normalized_cycle] + [normalized_cycle[-1][1]]

    def crossover(parent1, parent2):
        """Combine two parent cycles to produce a child cycle."""
        cut = random.randint(1, len(parent1) - 2)
        child = parent1[:cut] + [node for node in parent2 if node not in parent1[:cut]]
        return child

    def mutate(cycle):
        """Mutate a cycle by swapping two random nodes."""
        cycle = cycle[:]  # Copy the cycle to avoid mutating the original
        i, j = random.sample(range(len(cycle)), 2)
        cycle[i], cycle[j] = cycle[j], cycle[i]
        return cycle

    n = len(adj_matrix)
    nodes = list(range(n))
    unique_cycles = set()  # Store normalized cycles for uniqueness
    population = []

    # Initialize population with valid random cycles
    while len(population) < population_size:
        random.shuffle(nodes)
        if is_valid_cycle(nodes):
            normalized_cycle = normalize_cycle(nodes, is_directed)
            if normalized_cycle not in unique_cycles:
                unique_cycles.add(normalized_cycle)
                population.append(nodes[:])  # Store the actual cycle

    for _ in range(generations):
        # Fitness evaluation: Filter only valid cycles
        population = [cycle for cycle in population if is_valid_cycle(cycle)]

        # Normalize and deduplicate
        normalized_population = {normalize_cycle(cycle, is_directed) for cycle in population}
        unique_cycles.update(normalized_population)
        population = [cycle_from_normalized(normalized_cycle) for normalized_cycle in normalized_population]

        # Refill population if necessary
        while len(population) < population_size:
            random.shuffle(nodes)
            if is_valid_cycle(nodes):
                normalized_cycle = normalize_cycle(nodes, is_directed)
                if normalized_cycle not in unique_cycles:
                    unique_cycles.add(normalized_cycle)
                    population.append(nodes[:])

        # Selection
        selected = random.sample(population, min(len(population), population_size // 2))

        # Crossover and mutation
        new_population = []
        for i in range(len(selected) - 1):
            parent1 = selected[i]
            parent2 = selected[i + 1]
            child = mutate(crossover(parent1, parent2))
            if is_valid_cycle(child):
                new_population.append(child)

        population.extend(new_population)

    return len(unique_cycles)
