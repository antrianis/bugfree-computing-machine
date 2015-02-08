def duplicate_count(text):
    r = [0] * 26
    text = text.lower()
    for t in text:
        r[ord(t) - 97] += 1
    return sum(1 for l in r if l > 1)
