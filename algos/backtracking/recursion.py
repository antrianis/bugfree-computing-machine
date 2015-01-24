import pdb
def permutations(string):
     pdb.set_trace()
     if not string:
             return ['']
     ret = []
     for i, d in enumerate(string):
             perms = permutations(string[:i] + string[i+1:])
             for perm in perms:
                     ret.append(d + perm)
     return ret

print permutations('ela') 




