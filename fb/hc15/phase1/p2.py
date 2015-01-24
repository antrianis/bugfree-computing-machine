_end = '_end_'

def search(root,word):
    subroots=root[word]
    if len(subroots) > 1:
        return false
 
def make_trie(*words):
     root = dict()
     sum = 0
     for word in words:
         current_dict = root
         for letter in word:
             current_dict = current_dict.setdefault(letter, {})
         current_dict = current_dict.setdefault(_end, _end)
         up_to  = ''
         for letter in word:
             up_to+=letter
             r = search(current_dict,up_to)
             if r:
                 break
             else:
                 sum+=1
     return sum, root

print make_trie('hi', 'hello', 'lol', 'hills','hill')
