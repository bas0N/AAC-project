class GraphDistanceCalculator:
    """
    A class to calculate the distance between two graphs represented by adjacency matrices.
    """

    def __init__(self, is_directed=False):
        """
        Initialize the calculator with the graph directionality.

        :param is_directed: Boolean - True if graphs are directed, False if undirected.
        """
        self.is_directed = is_directed

    def calculate_distance(self, matrices):
        """
        Calculate the distance between two graphs.

        :param matrices: Tuple[List[List[int]], List[List[int]]] - A tuple containing adjacency matrices of graph A and graph B.
        :return: Integer - Minimum number of edge modifications required.
        """
        matrix_a, matrix_b = matrices  # Unpack the tuple

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
                    if not self.is_directed and i != j:
                        matrix_a[j][i] = matrix_b[j][i]  # Sync the symmetric change

        return distance
