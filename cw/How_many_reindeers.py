from math import ceil


def reindeer(presents):
    if presents > 180:
        raise ValueError('No Santa this year')
    return 2 + ceil(presents/30.0)
