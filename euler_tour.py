from collections import defaultdict



graph = defaultdict(list)
def edge(n, m):
    graph[n].append(m)
    graph[m].append(n)

def print_cycle_nodes(graph, node):
    print(graph)
    pass


cycle_node = None
def check_cycles(graph, node, visited, parent):
    global cycle_node
    visited[node] = True
    for n in graph[node]:
        if visited[n] is False:
            if check_cycles(graph, n, visited, node):
                if node >= cycle_node:
                    print(node, n)
                return True
        elif parent is not n:
            cycle_node = n
            print(node, n)
            return True
    return False

def find_cycle(graph):
    graph_len = len(graph)
    visited = [False] * graph_len
    parent = None
    node = 0
    if check_cycles(graph, node, visited, parent):
        return True
    return False


if find_cycle(graph):
    print("yes a cycle exists")
else:
    print("no cycle here")




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



edge(0, 1)
edge(1, 2)
edge(2, 3)
edge(3, 3)
#edge(4, 4)

#edge(4, 0)



if find_euler(graph):
    print("yes there's a euler cycle")
else:
    print("no euler")