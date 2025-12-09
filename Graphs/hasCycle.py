def hasCycle(graph):
    vis = set()
    def dfs(node, parent):
        vis.add(node)
        for nei in graph[node]:
            if nei not in vis:
                if dfs(nei, node):
                    return True
            elif nei != parent:
                return True
        return False
    for n in graph:
        if n not in vis:
            if dfs(n, -1):
                return True
    return False
