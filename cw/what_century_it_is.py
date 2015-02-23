def whatCentury(year):
    ordinals = {'1': 'st', "2": 'nd', "3": 'rd'}
    century = str(int(year) / 100 + (1 if int(year) % 100 > 0 else 0))
    return century + (ordinals.get(century[-1], 'th') if century[0] != '1' else 'th')


print whatCentury(str(1999))
print whatCentury('10')
print whatCentury('1')
print whatCentury('2000') == '20th'
