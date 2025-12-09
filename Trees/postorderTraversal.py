def postorderTraversal(root):
    if not root:
        return []
    s = [root]
    res = []
    while s:
        n = s.pop()
        res.append(n.val)
        if n.left:
            s.append(n.left)
        if n.right:
            s.append(n.right)
    return res[::-1]
