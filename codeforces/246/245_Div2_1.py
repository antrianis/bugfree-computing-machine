
if __name__ == '__main__':

    n, k = map(int, raw_input().split())
    participation = map(int, raw_input().split())

    participants = (x for x in participation if x + k <= 5)
    print len(list(participants)) / 3
