from operator import itemgetter


def ranks(a):
    if not len(a):
        return []
    r = [0] * len(a)

    indices, a_sorted = zip(*sorted(enumerate(a), key=itemgetter(1),
                                    reverse=True))
    current_rank, total_rank = 1, 1
    pre = a_sorted[0]
    for i, e in zip(indices, a_sorted):
        if pre != e:
            current_rank = total_rank
        r[i] = current_rank
        total_rank += 1
        pre = e
    return r


def ranks1(a):
    sorted_a = sorted(a, reverse=True)
    return [sorted_a.index(v) + 1 for v in a]

