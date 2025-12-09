def bfs(start, graph):
    from collections import deque
    q = deque([start])
    vis = set([start])
    res = []
    while q:
        n = q.popleft()
        res.append(n)
        for nei in graph[n]:
            if nei not in vis:
                vis.add(nei)
                q.append(nei)
    return res
