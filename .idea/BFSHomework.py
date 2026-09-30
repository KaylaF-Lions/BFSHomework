from collections import deque


def bfs_search(start, goal, max_state=15):
    queue = deque([start])
    visited = {start}
    expansion_order = []

    while queue:
        current = queue.popleft()
        expansion_order.append(current)

        if current == goal:
            print(f"Goal {goal} reached successfully!")
            return expansion_order

        successors = [2 * current, 2 * current + 1]

        for neighbor in successors:
            if neighbor not in visited and neighbor <= max_state:
                visited.add(neighbor)
                queue.append(neighbor)

    print("Goal not found in the defined state space.")
    return expansion_order

start_state = 1
goal_state = 11
steps = bfs_search(start_state, goal_state)

print("Nodes expanded in order:", steps)
