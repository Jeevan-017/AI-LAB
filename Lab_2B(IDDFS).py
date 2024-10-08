def iterative_depth_search(graph, start, goal):
   
    depth_limit = 1
    while True:
        stack = [(start, [start])]
        while stack:
            node, path = stack.pop()
            if node == goal:
                return path
            if len(path) < depth_limit:  
                for neighbor in graph[node]:
                    if neighbor not in path:  # Avoid cycles
                        stack.append((neighbor, path + [neighbor]))
        depth_limit += 1

# Example usage:
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': ['H'],
    'E': ['I'],
    'F': [],
    'G': ['J'],
    'J': []
}

start_node = 'A'
goal_node = 'G'

path = iterative_depth_search(graph, start_node, goal_node)
if path:
    print("Path found:", path)
else:
    print("No path found.")
