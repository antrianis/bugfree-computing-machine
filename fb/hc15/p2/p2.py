from itertools import combinations
t = int(raw_input())
for i in range(t):
    target = map(int, raw_input().split())
    target_sum0 = target[0]
    target_sum1 = target[1]
    target_sum2 = target[2]

    no_food = int(raw_input())
    f = []
    for _ in range(no_food):
        f.append(map(int, raw_input().split()))
    vals0 = [d[0] for d in f]
    vals1 = [d[1] for d in f]
    vals2 = [d[2] for d in f]

    done = False
    for clen in range(1, no_food+1):
        if done:
            break
        sum0 = sum1 = sum2 = 0
        for comb in combinations(range(no_food), clen):
            for index_c in comb:
                sum0 += vals0[index_c]
                sum1 += vals1[index_c]
                sum2 += vals2[index_c]
                if sum0 > target_sum0 or sum1 > target_sum1 or sum2 > target_sum2:
                    break
            if sum0 == target_sum0 and sum1 == target_sum1 and sum2 == target_sum2:
                print 'Case #{}: {} '.format(i+1, 'yes')
                done = True
                break
            sum0 = sum1 = sum2 = 0
    if not done:
        print 'Case #{}: {} '.format(i+1, 'no')

















