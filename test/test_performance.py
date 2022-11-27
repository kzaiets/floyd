import timeit
import src.floyd_imperative as floyd_i
import src.floyd_recursive as floyd_r
from .test_cases import graph_one_node, graph_2, graph_4, graph_5, graph_8, graph_9
graphs = [graph_one_node, graph_2, graph_4, graph_5, graph_8, graph_9]
fl = ['Imperative', 'Recursive']


# run performance tests for recursive and imperative versions
def performance_tests():
    for f in fl:
        print(f)
        # run function 10,000 times for graph with 1, 2, 4, 5, 8, and 9 nodes
        for graph in graphs:
            print(f'Graph with {len(graph[0])} nodes')
            if f == 'Imperative':
                def fld():
                    floyd_i.floyd(graph)
            else:
                def fld():
                    floyd_r.floyd(graph)
            times = timeit.repeat(
                                  stmt=fld,
                                  repeat=5,
                                  number=10000)
            # get average of 5 tries
            avrg = sum(times)/5
            print(times)
            print(f'average = {avrg}')


if __name__ == '__main__':
    performance_tests()
