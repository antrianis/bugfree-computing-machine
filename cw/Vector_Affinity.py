from itertools import izip_longest


def vector_affinity2(a, b):
    matches = [x == y for x, y in izip_longest(a, b, fillvalue=object())]
    return sum(matches) / float(len(matches)) if matches else 1


def vector_affinity(a, b):
    max_len = max(len(a), len(b))
    if max_len == 0:
        return 1
    return sum(1 for n, m in zip(a, b) if n == m) / float(max_len)
