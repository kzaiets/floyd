no_path = 500
graph = [[0, 5, no_path, 10],
         [no_path, 0, 3, no_path],
         [no_path, no_path, 0, 1],
         [no_path, no_path, no_path, 0]]


def floyd(dist):
    v = len(dist[0])
    for k in range(v):
        # pick all vertices as source one by one
        for i in range(v):
            # Pick all vertices as destination for the above picked source
            for j in range(v):
                # If vertex k is on the shortest path from
                # i to j, then update the value of dist[i][j]
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    return dist


if __name__ == '__main__':
    print(floyd(graph))
