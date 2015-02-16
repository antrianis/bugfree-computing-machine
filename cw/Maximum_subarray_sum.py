def maxSequence(numbers):
    if len(numbers) == 0:
        return 0
    max_till_here = [numbers[0]]
    for n in numbers[1:]:
        max_till_here.append(max(n, max_till_here[-1] + n))
    return max(max_till_here)


if __name__ == '__main__':
    assert maxSequence([1, -1]) == 1
    assert maxSequence([-2, -1, -3]) == -1
