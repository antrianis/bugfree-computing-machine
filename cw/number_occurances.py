def number_of_occurrences(s, xs):
        return sum(1 for e in xs if e == s)
