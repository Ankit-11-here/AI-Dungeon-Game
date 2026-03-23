from collections import deque

def bfs_next_step(grid, start, target):
    rows, cols = len(grid), len(grid[0])

    start = tuple(start)
    target = tuple(target)

    queue = deque([start])
    visited = set([start])
    parent = {}

    directions = [(1,0), (-1,0), (0,1), (0,-1)]

    while queue:
        r, c = queue.popleft()

        #If target reached → backtrack safely
        if (r, c) == target:
            # If target is same as start
            if target == start:
                return list(start)

            # Backtrack to find next step
            while parent.get((r, c)) != start:
                if (r, c) not in parent:
                    return list(start)  # safety check
                r, c = parent[(r, c)]

            return [r, c]

        # Explore neighbors
        for dr, dc in directions:
            nr = r + dr
            nc = c + dc

            # No wrap-around
            if 0 <= nr < rows and 0 <= nc < cols:
                if grid[nr][nc] != '#' and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    parent[(nr, nc)] = (r, c)
                    queue.append((nr, nc))

    #  If target unreachable → stay in same position
    return list(start)