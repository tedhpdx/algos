from collections import defaultdict

graph = defaultdict(list)
def edge(n, m):
    graph[n].append(m)
    graph[m].append(n)


def check_cycles(node, visited, parent):
    visited[node] = True
    for n in graph[node]:
        if visited[n] is False:
            if check_cycles(n, visited, node):
                return True
        elif parent is not n:
            return True
    return False



def find_cycle(graph):
    graph_len = len(graph)
    visited = [False] * graph_len
    parent = None
    for node in range(graph_len):
        if visited[node] is False:
            if check_cycles(node, visited, parent):
                return True
    return False






edge(0,1)
edge(1,0)
edge(3,4)
edge(4,5)

if find_cycle(graph):
    print("yes a cycle exists")
else:
    print("no cycle here")
