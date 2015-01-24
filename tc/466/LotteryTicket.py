def buy(price,b1,b2,b3,b4):
    bank_notes = [b1,b2,b3,b4]
    print buy_helper(price, bank_notes)

def buy_helper(price,bank_notes, cbank = []):
    if price == sum(cbank):
        return "POSSIBLE"

    for b in bank_notes:
        t = cbank
        t.append(b)
        buy_helper(price,bank_notes,t)
        buy_helper(price,bank_notes,cbank)

    return "IMPOSSIBLE"
buy(10,1,5,10,50)
