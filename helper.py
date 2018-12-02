"""
A package helper with various useful functions
"""

def permute(items, low=0):
    """Returns all permutations of a list of items"""
    if low + 1 >= len(items):
        yield items
    else:
        for perm in permute(items, low + 1):
            yield perm
        for k in range(low + 1, len(items)):
            items[low], items[k] = items[k], items[low]
            for perm in permute(items, low + 1):
                yield perm
            items[low], items[k] = items[k], items[low]
