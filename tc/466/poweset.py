def buy(price,b1,b2,b3,b4):
    bank_notes = [b1,b2,b3,b4]
    print buy_helper(price, bank_notes)

def buy_helper(a,price):

    if (sum(a) == price):
        return "POSSIBLE"

    if (len(a) == 0):
        return [[]]
    else:
        allSubsets = [ ]
        for subset in powerset(a[1:],price):
            allSubsets += [subset]
            allSubsets += [[a[0]] + subset]
        return allSubsets

print powerset([1,2,3])
