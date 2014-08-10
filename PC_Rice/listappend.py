def appendsums(lst):
    """
    Repeatedly append the sum of the current last three elements of lst to lst.
    """
    for _ in range(25):
        lst.append(sum(lst[-3:]))

if __name__ == "__main__":
    sum_three = [0, 1, 2]
    appendsums(sum_three)
    print sum_three[20]
