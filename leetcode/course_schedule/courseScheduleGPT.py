class Solution(object):
    from collections import deque, defaultdict

def is_cyclic_bfs(num_nodes, edges):
    graph = defaultdict(list)
    in_degree = [0] * num_nodes

    # Build graph and compute in-degrees
    for u, v in edges:
        graph[u].append(v)
        in_degree[v] += 1

    # Enqueue nodes with 0 in-degree
    queue = deque([node for node in range(num_nodes) if in_degree[node] == 0])
    visited_count = 0

    while queue:
        current = queue.popleft()
        visited_count += 1
        for neighbor in graph[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    # If not all nodes were visited, there is a cycle
    return visited_count != num_nodes
