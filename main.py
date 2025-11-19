"""
HW05 — Warehouse Robot Path (Grid BFS)

Implement:
- parse_grid(lines)
- grid_shortest_path(lines)
"""

from collections import deque

def parse_grid(lines):
    """Return (graph, start, target) built from the grid lines.

    Graph keys are "r,c" strings for open cells. Neighbors move 4 directions.
    """

    graph = {}
    start = None
    target = None

    rows = len(lines)
    cols = len(lines[0]) if rows > 0 else 0

    # Directions: up, down, left, right
    dirs = [(-1,0), (1,0), (0,-1), (0,1)]

    for r in range(rows):
        for c in range(cols):
            ch = lines[r][c]
            if ch == '#':
                continue

            key = f"{r},{c}"
            graph[key] = []

            if ch == 'S':
                start = key
            if ch == 'T':
                target = key

    # Build neighbors
    for r in range(rows):
        for c in range(cols):
            if lines[r][c] == '#':
                continue

            key = f"{r},{c}"
            for dr, dc in dirs:
                rr = r + dr
                cc = c + dc
                if 0 <= rr < rows and 0 <= cc < cols:
                    if lines[rr][cc] != '#':
                        nbr = f"{rr},{cc}"
                        graph[key].append(nbr)

    return graph, start, target


def grid_shortest_path(lines):
    """Return a shortest path list of "r,c" from S to T; or None if unreachable."""

    graph, start, target = parse_grid(lines)

    if start is None or target is None:
        return None

    # If start equals target, return path with just the start position
    if start == target:
        return [start]

    # BFS to find shortest path
    queue = deque([(start, [start])])
    visited = {start}

    while queue:
        current, path = queue.popleft()

        if current == target:
            return path

        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))

    return None
