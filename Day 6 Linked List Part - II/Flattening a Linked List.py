def merge(a, b):
    if not a:
        return b
    if not b:
        return a

    ans = None
    if a.data < b.data:
        ans = a
        ans.bottom = merge(a.bottom, b)
    else:
        ans = b
        ans.bottom = merge(a, b.bottom)

    return ans

def flatten(root):
    if not root:
        return None

    mergedLL = merge(root, flatten(root.next))
    return mergedLL