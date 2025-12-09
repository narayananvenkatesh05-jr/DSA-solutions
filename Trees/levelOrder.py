def levelOrder(root):
    from collections import deque
    if not root:
        return []
    q = deque([root])
    res = []
    while q:
        temp = []
        for _ in range(len(q)):
            n = q.popleft()
            temp.append(n.val)
            if n.left:
                q.append(n.left)
            if n.right:
                q.append(n.right)
        res.append(temp)
    return res
