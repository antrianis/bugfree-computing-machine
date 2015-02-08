
def disemvowel(s):

    for v in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
        s = s.replace(v, '')
    return s
