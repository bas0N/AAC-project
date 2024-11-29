class GraphSizeCalculator:
    def __init__(self):
        """
        Utility class for calculating the size of a graph based on its adjacency matrix.
        """
        pass

    @staticmethod
    def graph_size(input):
        """
        Calculate the size (number of edges) of a graph.

        :param adjacency_matrix: The adjacency matrix representing the graph.
        :param is_directed: A boolean indicating if the graph is directed.
        :return: The number of edges in the graph.
        """
        adjacency_matrix, is_directed = input
        if is_directed:
            # Count all edges in a directed graph
            return sum(sum(row) for row in adjacency_matrix)
        else:
            # Count only the upper triangle for undirected graphs (no double counting)
            return sum(sum(row[:i + 1]) for i, row in enumerate(adjacency_matrix))
