from collections import defaultdict

graph = defaultdict(list)
def edge(n, m):
    graph[n].append(m)
    graph[m].append(n)


def top_sort_SSC(SCC_list):
    return 0

def find_SCC(graph):
    return 0

def create_graph_of_SCC(SCC_List):
    return {}


def dfs(graph, node, visited_nodes):
    visited_nodes.append(node)
    for n in graph[node]:
        if n not in visited_nodes:
            dfs(graph, n, visited_nodes)

def check_if_semi_connected(graph):
    SCC_list = find_SCC(graph)
    _graph = create_graph_of_SCC(SCC_list)
    starting_node = top_sort_SSC(SCC_list)
    visited_nodes = []
    dfs(_graph, starting_node, visited_nodes)
    if len(visited_nodes) == len(graph):
        return True
    else:
        return False




edge(0,1)
edge(1,2)
edge(1,3)
edge(3,4)
edge(4,3)
edge(5,7)

print(check_if_semi_connected(graph))


