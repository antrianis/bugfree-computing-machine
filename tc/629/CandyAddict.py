# -*- coding: utf-8 -*-
import math,string,itertools,fractions,heapq,collections,re,array,bisect

class CandyAddict:
    def solve(self, X, Y, Z):
        result = []
        for q in range(len(Z)):
            candies = 0
            x = X[q]
            y = Y[q]
            dollars = 0
            for z in range(Z[q]):
                dollars += x
                if candies == 0:
                    new_candies = dollars / y
                    candies += new_candies
                    dollars -= new_candies * y
                candies-=1
            result.append(dollars)
        return result

# CUT begin
# TEST CODE FOR PYTHON {{{
import sys, time, math

def tc_equal(expected, received):
    try:
        _t = type(expected)
        received = _t(received)
        if _t == list or _t == tuple:
            if len(expected) != len(received): return False
            return all(tc_equal(e, r) for (e, r) in zip(expected, received))
        elif _t == float:
            eps = 1e-9
            d = abs(received - expected)
            return not math.isnan(received) and not math.isnan(expected) and d <= eps * max(1.0, abs(expected))
        else:
            return expected == received
    except:
        return False

def pretty_str(x):
    if type(x) == str:
        return '"%s"' % x
    elif type(x) == tuple:
        return '(%s)' % (','.join( (pretty_str(y) for y in x) ) )
    else:
        return str(x)

def do_test(X, Y, Z, __expected):
    startTime = time.time()
    instance = CandyAddict()
    exception = None
    try:
        __result = instance.solve(X, Y, Z);
    except:
        import traceback
        exception = traceback.format_exc()
    elapsed = time.time() - startTime   # in sec

    if exception is not None:
        sys.stdout.write("RUNTIME ERROR: \n")
        sys.stdout.write(exception + "\n")
        return 0

    if tc_equal(__expected, __result):
        sys.stdout.write("PASSED! " + ("(%.3f seconds)" % elapsed) + "\n")
        return 1
    else:
        sys.stdout.write("FAILED! " + ("(%.3f seconds)" % elapsed) + "\n")
        sys.stdout.write("           Expected: " + pretty_str(__expected) + "\n")
        sys.stdout.write("           Received: " + pretty_str(__result) + "\n")
        return 0

def run_tests():
    sys.stdout.write("CandyAddict (1000 Points)\n\n")

    passed = cases = 0
    case_set = set()
    for arg in sys.argv[1:]:
        case_set.add(int(arg))

    with open("CandyAddict.sample", "r") as f:
        while True:
            label = f.readline()
            if not label.startswith("--"): break

            X = []
            for i in range(0, int(f.readline())):
                X.append(int(f.readline().rstrip()))
            X = tuple(X)
            Y = []
            for i in range(0, int(f.readline())):
                Y.append(int(f.readline().rstrip()))
            Y = tuple(Y)
            Z = []
            for i in range(0, int(f.readline())):
                Z.append(int(f.readline().rstrip()))
            Z = tuple(Z)
            f.readline()
            __answer = []
            for i in range(0, int(f.readline())):
                __answer.append(int(f.readline().rstrip()))
            __answer = tuple(__answer)

            cases += 1
            if len(case_set) > 0 and (cases - 1) in case_set: continue
            sys.stdout.write("  Testcase #%d ... " % (cases - 1))
            passed += do_test(X, Y, Z, __answer)

    sys.stdout.write("\nPassed : %d / %d cases\n" % (passed, cases))

    T = time.time() - 1407857406
    PT, TT = (T / 60.0, 75.0)
    points = 1000 * (0.3 + (0.7 * TT * TT) / (10.0 * PT * PT + TT * TT))
    sys.stdout.write("Time   : %d minutes %d secs\n" % (int(T/60), T%60))
    sys.stdout.write("Score  : %.2f points\n" % points)

if __name__ == '__main__':
    run_tests()

# }}}
# CUT end
