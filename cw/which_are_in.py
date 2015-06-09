def in_array(a1, a2):
    return sorted({sub for sub in a1 if any(sub in s for s in a2)})
