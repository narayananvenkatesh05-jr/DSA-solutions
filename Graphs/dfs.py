def dfs(start, graph):
    stack = [start]
    vis = set()
    res = []
    while stack:
        n = stack.pop()
        if n not in vis:
            vis.add(n)
            res.append(n)
            for nei in graph[n]:
                stack.append(nei)
    return res
