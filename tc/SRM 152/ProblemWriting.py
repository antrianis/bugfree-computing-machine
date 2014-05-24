# -*- coding: utf-8 -*-
import math,string,itertools,fractions,heapq,collections,re,array,bisect

class ProblemWriting:
    def isdigit(self,s):
        try:
            n = int(s)
            return len(s) == 1
        except ValueError:
            return 0

    def myCheckData(self, dotForm):
        s = 0
        if len(dotForm) == 0 or len(dotForm) > 25:
            return "dotForm must contain between 1 and 25 characters, inclusive."
        i = 0
        for c in dotForm:
            if s == 0:
                s = 1 if self.isdigit(c) else -1
            elif s == 1:
                if c == ".":
                    s = 2
                elif c == '+' or c == '-' or c == '*' or c == '/':
                    s = 3
                else:
                    s = -1
            elif s == 2:
                if c == ".":
                    s = 2
                elif c == '+' or c == '-' or c == '*' or c == '/':
                    s = 3
                else:
                    s = -1
            elif s == 3:
                if c == ".":
                    s = 3
                elif self.isdigit(c):
                    s = 1
                else:
                    s = -1
            if s == -1:
                return "dotForm is not in dot notation, check character " + str(i) + "."
            i+=1
        if s != 1:
            return "dotForm is not in dot notation, check character " + str(len(dotForm)) + "."
        else:
            return ""
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

def do_test(dotForm, __expected):
    startTime = time.time()
    instance = ProblemWriting()
    exception = None
    try:
        __result = instance.myCheckData(dotForm);
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
    sys.stdout.write("ProblemWriting (1000 Points)\n\n")

    passed = cases = 0
    case_set = set()
    for arg in sys.argv[1:]:
        case_set.add(int(arg))

    with open("ProblemWriting.sample", "r") as f:
        while True:
            label = f.readline()
            if not label.startswith("--"): break

            dotForm = f.readline().rstrip()
            f.readline()
            __answer = f.readline().rstrip()

            cases += 1
            if len(case_set) > 0 and (cases - 1) in case_set: continue
            sys.stdout.write("  Testcase #%d ... " % (cases - 1))
            passed += do_test(dotForm, __answer)

    sys.stdout.write("\nPassed : %d / %d cases\n" % (passed, cases))

    T = time.time() - 1400934163
    PT, TT = (T / 60.0, 75.0)
    points = 1000 * (0.3 + (0.7 * TT * TT) / (10.0 * PT * PT + TT * TT))
    sys.stdout.write("Time   : %d minutes %d secs\n" % (int(T/60), T%60))
    sys.stdout.write("Score  : %.2f points\n" % points)

if __name__ == '__main__':
    run_tests()

# }}}
# CUT end
