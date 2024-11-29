import random

class InputGeneratorUtil:
    def generate_random_graph(self, num_vertices, is_directed=None, seed=None):
        """
        Generate a single random graph and return it as a formatted string.

        :param num_vertices: Number of vertices in the graph.
        :param is_directed: Boolean indicating if the graph is directed. If None, randomly decide.
        :param seed: Seed for the random number generator. If None, use the default randomness.
        :return: A tuple containing a boolean (is_directed) and a string representing the graph.
        """
        # Use a local random generator for this function
        local_random = random.Random(seed)

        # Decide if the graph is directed
        if is_directed is None:
            is_directed = local_random.choice([True, False])

        adjacency_matrix = []

        # Generate the adjacency matrix
        for i in range(num_vertices):
            row = []
            for j in range(num_vertices):
                if i == j:
                    row.append(0)  # No self-loops
                else:
                    if is_directed:
                        # Randomly assign edge weights for directed graphs
                        row.append(local_random.randint(0, 1))
                    else:
                        # Ensure symmetry for undirected graphs
                        row.append(local_random.randint(0, 1) if i < j else adjacency_matrix[j][i])
            adjacency_matrix.append(row)

        # Build the textual representation
        graph_text = f"{num_vertices}\n"
        graph_text += "\n".join(" ".join(map(str, row)) for row in adjacency_matrix)

        return is_directed, graph_text
