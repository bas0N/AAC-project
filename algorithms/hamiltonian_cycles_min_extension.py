## minimal extension (bruteforce)
from itertools import permutations, combinations

def is_valid_cycle(path, adj_matrix):
    """Check if the path is a valid Hamiltonian cycle."""
    for i in range(len(path)):
        u, v = path[i], path[(i + 1) % len(path)]  # Cycle wraps back to the start
        if adj_matrix[u][v] == 0:  # No edge between consecutive nodes
            return False
    return True

def is_hamiltonian(adj_matrix):
    """Check if the graph contains a Hamiltonian cycle."""
    n = len(adj_matrix)

    # Check if any permutation forms a Hamiltonian cycle
    for perm in permutations(range(n)):
        if is_valid_cycle(perm, adj_matrix):
            return True
    return False

def make_hamiltonian(adj_matrix, directed=False):
    """
    Return the minimal number of edges needed to make the graph Hamiltonian.
    """
    # Check if the graph is already Hamiltonian
    if is_hamiltonian(adj_matrix):
        return 0  # No edges needed

    n = len(adj_matrix)
    # Generate all potential edges that can be added (only where no edge exists)
    edges = [(i, j) for i in range(n) for j in range(n) if i != j and adj_matrix[i][j] == 0]

    # Try adding k edges
    for k in range(1, len(edges) + 1):
        for edge_combination in combinations(edges, k):
            # Create a copy of the adjacency matrix
            new_matrix = [row[:] for row in adj_matrix]

            # Add the edges
            for u, v in edge_combination:
                new_matrix[u][v] = 1
                if not directed:  # For undirected graphs, add the reverse edge
                    new_matrix[v][u] = 1

            # Check if the new graph is Hamiltonian
            if is_hamiltonian(new_matrix):
                return k  # Return the minimal number of edges needed

    # If no solution, return -1 (this should not happen for a connected graph)
    return -1



## minimal extension (approximation)
from itertools import combinations
import random

def is_valid_cycle(path, adj_matrix):
    """
    Check if the given path forms a valid Hamiltonian cycle.
    A Hamiltonian cycle visits every node exactly once and returns to the starting node.
    """
    for i in range(len(path)):
        u, v = path[i], path[(i + 1) % len(path)]  # Wrap around for cyclic path
        if adj_matrix[u][v] == 0:  # No edge between consecutive nodes
            return False
    return True

def approximate_hamiltonian_cycle(adj_matrix):
    """
    Approximate whether the graph contains a Hamiltonian cycle using a greedy traversal.
    """
    n = len(adj_matrix)
    visited = set()
    stack = [0]  # Start from node 0

    while stack:
        current = stack.pop()
        visited.add(current)
        for neighbor in range(n):
            if adj_matrix[current][neighbor] == 1 and neighbor not in visited:
                stack.append(neighbor)

    # Check if all nodes are visited and the last visited node connects back to the first
    return len(visited) == n and adj_matrix[current][0] == 1

def make_hamiltonian_heuristic(adj_matrix, directed=False, max_iterations=1000):
   """
    Approximate the minimal number of edges needed to make the graph Hamiltonian.

    Heuristics Used:
        1. **Degree Heuristic:** Nodes with fewer connections are prioritized for edge addition,
           as they are more likely to be isolated or disconnected from a potential cycle.
        2. **Random Sampling:** Instead of checking all combinations of edges exhaustively,
           randomly sample subsets of edge combinations and evaluate their impact.
        3. **Greedy Traversal:** Use an approximate Hamiltonian cycle detector to reduce
           computational overhead compared to testing all permutations.

    Args:
        adj_matrix: The adjacency matrix of the graph.
        directed: If True, consider the graph as directed; otherwise, undirected.
        max_iterations: The maximum number of edge combinations to sample for each k.

    Returns:
        int: The approximate minimal number of edges needed to make the graph Hamiltonian,
             or -1 if no solution is found (unlikely for connected graphs).
    """
    # Step 1: Check if the graph is already Hamiltonian
    if approximate_hamiltonian_cycle(adj_matrix):
        return 0  # No edges needed if the graph is already Hamiltonian

    n = len(adj_matrix)
    edges = [(i, j) for i in range(n) for j in range(n) if i != j and adj_matrix[i][j] == 0]

    # Step 2: Prioritize low-degree nodes for edge addition
    degree = [sum(adj_matrix[i]) for i in range(n)]
    edges = sorted(edges, key=lambda x: (degree[x[0]] + degree[x[1]]))  # Degree heuristic

    # Step 3: Iteratively try adding k edges
    for k in range(1, len(edges) + 1):
        for edge_combination in random.sample(list(combinations(edges, k)), min(max_iterations, len(list(combinations(edges, k))))):
            # Create a new adjacency matrix with the additional edges
            new_matrix = [row[:] for row in adj_matrix]
            for u, v in edge_combination:
                new_matrix[u][v] = 1
                if not directed:
                    new_matrix[v][u] = 1

            # Check if the new graph is approximately Hamiltonian
            if approximate_hamiltonian_cycle(new_matrix):
                return k  # Return the minimal number of edges needed

    # If no solution is found, return -1 (should not happen for connected graphs)
    return -1

