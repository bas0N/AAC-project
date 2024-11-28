import random

class GeneratorUtil:
    def __init__(self):
        """
        Utility class for generating random graph input data.
        """
        pass

    def generate_random_input(self, number_of_graphs, num_vertices):
        """
        Generate random graph input data.

        :param number_of_graphs: Number of graphs to generate.
        :param num_vertices: Number of vertices in each graph.
        :return: A string representing the input data.
        """
        input_data = f"{number_of_graphs}\n"

        for _ in range(number_of_graphs):
            is_directed = random.choice([True, False])

            input_data += f"{num_vertices}\n"
            adjacency_matrix = []

            for i in range(num_vertices):
                row = []
                for j in range(num_vertices):
                    if i == j:
                        row.append(0)  # No self-loops
                    else:
                        if is_directed:
                            row.append(random.randint(0, 1))
                        else:
                            # Ensure symmetry for undirected graphs
                            row.append(random.randint(0, 1) if i < j else adjacency_matrix[j][i])
                adjacency_matrix.append(row)

            # Add matrix to input
            input_data += "\n".join(" ".join(map(str, row)) for row in adjacency_matrix) + "\n"

        return input_data
