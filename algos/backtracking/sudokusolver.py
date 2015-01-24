def test_sorted(nums):
    prev = -1
    for n in nums:
        if n < prev:
            return False
    return True

def sortnumber(inums, onums):

    #The bad case
    if len(onums) > 0:
        if not test_sorted(inums):
            return False

    #The good case
    if len(onums) == len(inums):
        if test_sorted(inums):
            print "Solved!: " , onums
            return True

    # The backtracking        
    for n in inums:
        inums.remove(n)
        onums.append(n)
        print "inums" , inums
        print "onums", onums
        r = sortnumber(inums,onums)
        if r:
            return r
    return False


sortnumber([3,4,1],[])





