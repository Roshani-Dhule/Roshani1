import sys


def primMST(graph):
    V = len(graph)
    key = [sys.maxsize] * V
    parent = [None] * V
    key[0] = 0
    mstSet = [False] * V

    for _ in range(V):
        u = minKey(key, mstSet)
        mstSet[u] = True
        for v in range(V):
            if (
                graph[u][v] > 0
                and not mstSet[v]
                and key[v] > graph[u][v]
            ):
                key[v] = graph[u][v]
                parent[v] = u

    printMST(graph, parent)


def minKey(key, mstSet):
    min_val = sys.maxsize
    min_index = -1
    for v in range(len(key)):
        if key[v] < min_val and not mstSet[v]:
            min_val = key[v]
            min_index = v
    return min_index


def printMST(graph, parent):
    print("Edge \tWeight")
    for v in range(1, len(graph)):
        print(parent[v], "-", v, "\t", graph[v][parent[v]])


# Driver's code
if __name__ == "__main__":
    graph = [
        [0, 2, 0, 6, 0],
        [2, 0, 3, 8, 5],
        [0, 3, 0, 0, 7],
        [6, 8, 0, 0, 9],
        [0, 5, 7, 9, 0]
    ]

    primMST(graph)
