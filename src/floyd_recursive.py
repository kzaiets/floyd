# initial matrix
no_path = 500
graph = [[0, 5, no_path, 10],
         [no_path, 0, 3, no_path],
         [no_path, no_path, 0, 1],
         [no_path, no_path, no_path, 0]]


def floyd(dist):
    """
    Takes in the matrix and runs the matrix through a function to find the shortest distances between nodes
    """
    # Get the number of vertices of the input graph
    max_length = len(dist[0])
    # Subtracting 1 to avoid the increment over the max_length value
    v = max_length - 1
    return floyd_recursive(0, 0, 0, dist, v)


def floyd_recursive(inter_node, start_node, end_node, dist, v):
    """
    Takes in the values for start, end and intermediate nodes, which should be set to zero and the number of nodes,
    returns the matrix with the shortest distances between every pair of nodes
    """
    # Assume that if start_node and end_node are the same then the distance would be zero
    if start_node == end_node:
        dist[start_node][end_node] = 0
    else:
        # If inter_node is on the shortest path from start_node to end_node,
        # then update the value of dist[start_node][end_node]
        dist[start_node][end_node] = min(dist[start_node][end_node], dist[start_node][inter_node]
                                         + dist[inter_node][end_node])
    # Simulating for loops with if statements and increments
    if end_node < v:
        end_node += 1
        dist = floyd_recursive(inter_node, start_node, end_node, dist, v)

    elif start_node < v:
        end_node = 0
        start_node += 1
        dist = floyd_recursive(inter_node, start_node, end_node, dist, v)

    elif inter_node < v:
        start_node = 0
        end_node = 0
        inter_node += 1
        dist = floyd_recursive(inter_node, start_node, end_node, dist, v)
    return dist


if __name__ == '__main__':
    # Calls the function floyd and passes the graph
    print(floyd(graph))


