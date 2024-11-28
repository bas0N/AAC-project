import time

class TestingUtil:
    def __init__(self, testing_function):
        """
        Initialize the TestingUtil with a testing function.

        :param testing_function: A function that takes an adjacency matrix as input
                                 and performs some operation.
        """
        self.testing_function = testing_function

    def run_test(self, adjacency_matrix, test_name="Unnamed Test"):
        """
        Run the testing function on the given adjacency matrix and calculate its execution time.

        :param adjacency_matrix: The adjacency matrix to test.
        :param test_name: The name of the test (default is "Unnamed Test").
        :return: A tuple containing the result of the testing function and its execution time.
        """
        print(f"Running test: {test_name}")
        start_time = time.perf_counter()
        result = self.testing_function(adjacency_matrix)
        end_time = time.perf_counter()
        execution_time = end_time - start_time
        print(f"Test '{test_name}' completed in {execution_time:.6f} seconds")
        return result, execution_time