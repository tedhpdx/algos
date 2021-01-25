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


def find_euler(graph):
    graph_len = len(graph)
    euler_node_count = 0
    for i in range(graph_len):
        if len(graph[i]) % 2 is 0:
            euler_node_count += 1
    if euler_node_count == graph_len:
        return True
    else:
        return False



edge(1, 0)
edge(0, 2)
edge(2, 1)
edge(0, 3)
edge(3, 4)
#edge(4, 0)

if find_cycle(graph):
    print("yes a cycle exists")
else:
    print("no cycle here")

if find_euler(graph):
    print("yes there's a euler cycle")
else:
    print("no euler")