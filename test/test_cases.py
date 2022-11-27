no_path = 500
# 1 node
graph_one_node = [[0]]
# 2 nodes
graph_2 = [[0, no_path],
           [8, 0]]
# 4 nodes
graph_4 = [[0, 5, no_path, 10],
           [no_path, 0, 3, no_path],
           [no_path, no_path, 0, 1],
           [no_path, no_path, no_path, 0]]
# 4 nodes output
graph_4_output = [[0, 5, 8, 9],
                  [no_path, 0, 3, 4],
                  [no_path, no_path, 0, 1],
                  [no_path, no_path, no_path, 0]]
# 5 nodes
graph_5 = [[0, no_path, 3, no_path, no_path],
           [4, 0, no_path, 1, 2],
           [3, 8, 0, 2, 6],
           [no_path, 1, no_path, 0, 4],
           [no_path, 1, 6, 4, 0]]
# 8 nodes
graph_8 = [[0, 8, no_path, 19, 5, 3, 17, 21],
           [no_path, 0, no_path, 11, 5, no_path, 9, 13],
           [7, 4, 0, 15, 9, 4, 13, 17],
           [no_path, no_path, no_path, 0, 1, no_path, no_path, 2],
           [no_path, no_path, no_path, no_path, 0, no_path, no_path, no_path],
           [no_path, no_path, no_path, no_path, no_path, 0, no_path, no_path],
           [no_path, no_path, no_path, 3, 4, no_path, 0, 5],
           [no_path, no_path, no_path, no_path, no_path, no_path, no_path, 0]]
# 8 nodes output
graph_8_output = [[0, 8, 500, 19, 5, 3, 17, 21],
                  [500, 0, 500, 11, 5, 500, 9, 13],
                  [7, 4, 0, 15, 9, 4, 13, 17],
                  [500, 500, 500, 0, 1, 500, 500, 2],
                  [500, 500, 500, 500, 0, 500, 500, 500],
                  [500, 500, 500, 500, 500, 0, 500, 500],
                  [500, 500, 500, 3, 4, 500, 0, 5],
                  [500, 500, 500, 500, 500, 500, 500, 0]]
# 9 nodes
graph_9 = [[0, 8, no_path, no_path, 5, 3, no_path, no_path, 5],
           [no_path, 0, no_path, 11, 5, no_path, 9, no_path, no_path],
           [7, 4, 0, no_path, no_path, 4, no_path, no_path, 5],
           [4, 4, 8, 0, 1, no_path, no_path, 2, no_path],
           [4, 4, 8, no_path, 0, no_path, no_path, no_path, no_path],
           [4, 4, 8, no_path, no_path, 0, no_path, no_path, 7],
           [4, 4, 8, 3, no_path, 2, 0, 12, no_path],
           [4, 4, 8, no_path, no_path, no_path, no_path, 0, 5],
           [2, 8, 8, no_path, 5, 3, no_path, no_path, 0]]
graph_inc = [[0, 'no_path'],
             [9, no_path]]


