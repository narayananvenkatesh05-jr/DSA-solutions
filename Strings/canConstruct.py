def canConstruct(ransomNote, magazine):
    from collections import Counter
    r = Counter(ransomNote)
    m = Counter(magazine)
    return all(r[c] <= m[c] for c in r)
