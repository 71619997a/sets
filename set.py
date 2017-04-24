def diff(u, a):
    return [i for i in u if i not in a]

def union(a, b):
    return a + diff(b, a)

def intersection(a, b):
    return [i for i in a if i in b]

def symdiff(a, b):
    return diff(a, b) + diff(b, a)

def product(a, b):
    return [(i, j) for i in a for j in b]

a = [1, 2, 3]
b = [2, 3, 4]
print union(a, b)
print intersection(a, b)
print diff(a, b)
print diff(b, a)
print symdiff(a, b)
print product([1, 2], ['white', 'red'])
