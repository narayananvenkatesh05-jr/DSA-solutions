def cloneGraph(node):
    if not node:
        return None
    import collections
    d = {node: Node(node.val)}
    q = collections.deque([node])
    while q:
        n = q.popleft()
        for nei in n.neighbors:
            if nei not in d:
                d[nei] = Node(nei.val)
                q.append(nei)
            d[n].neighbors.append(d[nei])
    return d[node]
