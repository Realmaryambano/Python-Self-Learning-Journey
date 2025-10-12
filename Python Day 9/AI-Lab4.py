from queue import PriorityQueue

# Graph with nodes and edge costs
graph = {
    'S': [('A', 3), ('B', 6), ('C', 5)],
    'A': [('D', 6), ('F', 20)],
    'B': [('D', 2)],
    'C': [('E', 2)],
    'D': [('G', 4)],
    'E': [('G', 6)],
    'F': [('G', 1)],
    'G': []
}

# Heuristic values for each node (estimated cost to goal)
heuristics = {
    'S': 6,
    'A': 8,
    'B': 6,
    'C': 4,
    'D': 4,
    'E': 2,
    'F': 1,
    'G': 0
}

def a_star_search(start_node, goal_node):
    """
    A* search algorithm to find the path from start_node to goal_node.
    Uses a priority queue to select nodes based on f = g + h.
    """
    # Priority queue stores tuples: (f, g, current_node, path_so_far)
    pq = PriorityQueue()
    pq.put((heuristics[start_node], 0, start_node, [start_node]))

    visited_nodes = set()  # track visited nodes

    while not pq.empty():
        f_value, g_value, current, path_so_far = pq.get()

        # Skip if already visited
        if current in visited_nodes:
            continue
        visited_nodes.add(current)

        print(f"Visiting: {current}, g={g_value}, f={f_value}")  # optional: debug

        # If goal is reached, return the path
        if current == goal_node:
            return path_so_far

        # Explore neighbors
        for neighbor, cost in graph[current]:
            if neighbor not in visited_nodes:
                new_g = g_value + cost
                new_f = new_g + heuristics[neighbor]
                pq.put((new_f, new_g, neighbor, path_so_far + [neighbor]))

    return None  # goal not reachable

# Run the search
result = a_star_search('S', 'G')

if result:
    print("Path found:", " → ".join(result))
else:
    print("No path found from start to goal.")
