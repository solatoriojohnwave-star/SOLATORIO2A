from collections import deque


def build_graph():
    """
    Constructs the Graph from Assessment 3.3 (Diagram 2) using an adjacency list.
    O1 and O2 represent the first and second 'O' vertices so they remain distinct.
    Edges: S-O1, S-L, O1-A, O1-T, A-T, A-I, T-O2, L-O2, L-R, O2-R, R-I
    """
    graph = {
        "S": ["O1", "L"],
        "O1": ["S", "A", "T"],
        "L": ["S", "O2", "R"],
        "A": ["O1", "T", "I"],
        "T": ["O1", "A", "O2"],
        "O2": ["T", "L", "R"],
        "R": ["L", "O2", "I"],
        "I": ["A", "R"],
    }
    return graph


def format_vertex(vertex):
    """Converts O1/O2 back to O when displaying final letter output."""
    return "O" if vertex.startswith("O") else vertex


def bfs(graph, start):
    """Breadth-First Search starting from the given vertex."""
    visited = [start]
    queue = deque([start])

    while queue:
        current = queue.popleft()
        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.append(neighbor)
                queue.append(neighbor)

    return visited


def dfs(graph, current, visited=None):
    """Depth-First Search (Recursive) starting from the given vertex."""
    if visited is None:
        visited = []

    visited.append(current)

    for neighbor in graph[current]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

    return visited


if __name__ == "__main__":
    graph_data = build_graph()
    start_vertex = "S"

    bfs_visited = bfs(graph_data, start_vertex)
    dfs_visited = dfs(graph_data, start_vertex)

    bfs_letters = [format_vertex(v) for v in bfs_visited]
    dfs_letters = [format_vertex(v) for v in dfs_visited]

    print("Diagram 2: Graph Traversals")
    print("BFS (Vertices):", "-".join(bfs_visited))
    print("BFS (Letters): ", "-".join(bfs_letters))
    print("DFS (Vertices):", "-".join(dfs_visited))
    print("DFS (Letters): ", "-".join(dfs_letters))