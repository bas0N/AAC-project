import numpy as np
class GraphDistanceCalculator:
    """
    A class to calculate the distance between two graphs represented by adjacency matrices.
    """

    def __init__(self):
        """
        Initialize the calculator with the graph directionality.

        """

    def calculate_distance(self, matrices):
        """
        Calculate the distance between two graphs.

        :param matrices: Tuple[List[List[int]], List[List[int]]], is_directed:bool - A tuple containing adjacency matrices of graph A and graph B and a boolean indicating if the graphs are directed.
        :return: Integer - Minimum number of edge modifications required.

        """
        matrix_a, matrix_b, is_directed = matrices  # Unpack the tuple

        if len(matrix_a) != len(matrix_b):
            raise ValueError("Both adjacency matrices must have the same size.")

        num_vertices = len(matrix_a)
        distance = 0

        for i in range(num_vertices):
            for j in range(num_vertices):
                # Compare edges in both matrices
                if matrix_a[i][j] != matrix_b[i][j]:
                    distance += 1
                    # If undirected, ensure symmetry is considered
                    if not is_directed and i != j:
                        matrix_a[j][i] = matrix_b[j][i]  # Sync the symmetric change

        return distance