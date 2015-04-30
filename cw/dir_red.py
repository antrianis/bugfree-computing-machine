def dirReduc(arr):
    def opposites(a,b):
        if a == 'NORTH' and b == 'SOUTH' or a == 'SOUTH' and b == 'NORTH':
           return True
        if a == 'WEST' and b == 'EAST' or a == 'EAST' and b == 'WEST':
            return True
        return False

    while(True):
        found = False
        for i in range(len(arr)):
            if i + 1 < len(arr):
                if opposites(arr[i],arr[i+1]):
                    found = True
                    arr = arr[:i] + arr[i+2:]
        if not found:
            return arr
