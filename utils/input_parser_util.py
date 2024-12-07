class InputParserUtil:
    def __init__(self):
        self.graphs = []

    @staticmethod
    def is_graph_directed(adjacency_matrix):
        """
        Check if a graph is directed based on its adjacency matrix.
        """
        for i in range(len(adjacency_matrix)):
            for j in range(len(adjacency_matrix)):
                if adjacency_matrix[i][j] != adjacency_matrix[j][i]:
                    return True
        return False

    def parse_adjacency_matrix(self, lines, current_line, num_vertices):
        """
        Parse the adjacency matrix for a graph from the input lines.

        :param lines: List of input lines.
        :param current_line: Current line index.
        :param num_vertices: Number of vertices in the graph.
        :return: Tuple of adjacency matrix and updated current line index.
        """
        adjacency_matrix = []
        for _ in range(num_vertices):
            current_line += 1
            adjacency_matrix.append(list(map(int, lines[current_line].split())))
        return adjacency_matrix, current_line

    def parse_single_graph(self, input_data):
        """
        Parse a single graph from the input string.

        :param input_data: String containing the graph input data.
        :return: Parsed graph information.
        """
        lines = input_data.strip().split('\n')
        current_line = 0
        num_vertices = int(lines[current_line])
        adjacency_matrix, current_line = self.parse_adjacency_matrix(lines, current_line, num_vertices)
        is_directed = self.is_graph_directed(adjacency_matrix)
        graph = {
            'number_of_vertices': num_vertices,
            'adjacency_matrix': adjacency_matrix,
            'is_directed': is_directed
        }

        return graph

    def parse_multiple_graphs(self, input_data):
        """
        Parse multiple graphs from the input string.

        :param input_data: String containing the graph input data.
        :return: List of parsed graphs.
        """
        lines = input_data.strip().split('\n')
        current_line = 0
        number_of_graphs = int(lines[current_line])
        parsed_graphs = []

        for _ in range(number_of_graphs):
            current_line += 1
            num_vertices = int(lines[current_line])
            adjacency_matrix, current_line = self.parse_adjacency_matrix(lines, current_line, num_vertices)
            is_directed = self.is_graph_directed(adjacency_matrix)
            parsed_graphs.append({
                'number_of_vertices': num_vertices,
                'adjacency_matrix': adjacency_matrix,
                'is_directed': is_directed
            })

        return parsed_graphs

    def read_matrix_file(self, file_path: str):
        """
        Reads a file containing:
        - On the first line: an integer n (the dimension of the matrix).
        - On the next n lines: n integers per line, separated by spaces.

        Returns:
        --------
        n : int
            The dimension of the matrix.
        matrix : list of lists of int
            The matrix read from the file.
        """
        with open(file_path, 'r') as f:
          return f.read()


    def is_directed(adj):
        n = len(adj)
        for i in range(n):
            for j in range(n):
                if adj[i][j] != adj[j][i]:
                    return True  # Found a pair that breaks symmetry
        return False  # All pairs are symmetric

