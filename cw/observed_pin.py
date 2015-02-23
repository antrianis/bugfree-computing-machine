def get_pins(observed):
    possible = []
    p = {'1': ['2', '4'], '2': ['1', '3', '5'], '3': ['2', '6'],
         '4': ['1', '5', '7'], '5': ['2', '4', '6', '8'],
         '6': ['3', '5', '9'], '7': ['4', '8'], '8': ['5', '7', '9', '0'],
         '0': ['8'], '9': ['8', '6']}

    for o in observed:
        possible.append(p[o] + [int(o)])

    def solve(all_vals, current, level, target_level, result):
        if level == target_level:
            result.append(''.join(str(e) for e in current))
            return
        for v in all_vals[level]:
            current.append(v)
            solve(all_vals, current, level + 1, target_level, result)
            current = current[:level]

    result = []
    solve(possible, [], 0, len(observed), result)
    return result

print get_pins('8')
print get_pins('11')
print get_pins('58')
