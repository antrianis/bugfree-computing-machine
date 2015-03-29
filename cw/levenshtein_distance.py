def levenshtein(a ,b, i=0, j=0):
    if i == len(a):
        return len(b) - j
    if j == len(b):
        return len(a) - i
    
    if a[i] == b[j]:
        return levenshtein(a ,b, i + 1, j + 1)
    else:
        return 1 + min (levenshtein(a ,b, i + 1, j),
        levenshtein(a, b, i, j+1), levenshtein(a, b, i+1, j+1))
        
    
        
