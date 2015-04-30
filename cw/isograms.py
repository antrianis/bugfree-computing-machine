def is_isogram(str):
    return len(set(str.lower())) == len(str.lower())
