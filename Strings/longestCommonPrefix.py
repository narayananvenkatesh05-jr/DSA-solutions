def longestCommonPrefix(strs):
    res = strs[0]
    for s in strs[1:]:
        while not s.startswith(res):
            res = res[:-1]
            if not res:
                return ""
    return res
