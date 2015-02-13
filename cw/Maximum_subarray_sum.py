def maxSequence(arr):
    if not arr:
        return 0
    max_till_here = [0]
    for n in arr:
        max_till_here.append(max(n, max_till_here[-1] + n))
    return max(max_till_here)


if __name__ == '__main__':
    print maxSequence([1,-1])
    assert maxSequence([1,-1]) == 1
