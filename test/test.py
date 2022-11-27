import unittest
import src.floyd_recursive as floyd
from .test_cases import graph_4, graph_4_output, graph_8, graph_8_output, graph_one_node, graph_inc


class TestRecursion(unittest.TestCase):
    def test_floyd_function(self):
        # test different cases
        self.assertEqual(floyd.floyd(graph_4), graph_4_output)
        self.assertEqual(floyd.floyd(graph_8), graph_8_output)

        # test a case where there is only one node
        self.assertEqual(floyd.floyd(graph_one_node), graph_one_node)

    def test_input_fails(self):
        # test if a function fails when receiving an invalid input
        with self.assertRaises(TypeError):
            floyd.floyd(graph_inc)


if __name__ == '__main__':
    unittest.main()
