import heapq

def astar(start, goal):
    queue = []
    heapq.heappush(queue, (0, start))
    path = {}
    cost = {start: 0}

    while queue:
        f, node = heapq.heappop(queue)

        if node == goal:
            result = []
            while node in path:
                result.append(node)
                node = path[node]
            result.append(start)
            return result[::-1]

        for next in neighbors(node):
            newcost = cost[node] + 1
            if next not in cost or newcost < cost[next]:
                path[next] = node
                cost[next] = newcost
                total = newcost + guess(next, goal)
                heapq.heappush(queue, (total, next))

    return None

def guess(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def neighbors(node):
    x, y = node
    return [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]

start = (0, 0)
goal = (3, 3)
print("Path:", astar(start, goal))
