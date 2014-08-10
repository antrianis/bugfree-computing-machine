
def add_ball(balls, i, k):
    return balls[:i] + [k] + balls[i:]


def remove_balls(balls, i):
    return balls[:i] + balls[i + 1:]

def destroy(balls,n,i):
    myball = 0
    for i in xrange(n-2):
        #print i
        if balls[i] == balls[i+1] == balls[i+2]:
            start = i
            end = i + 2
            while (end + 1 < n and balls[end] == balls[end + 1]):
                end+=1
            if (i>=start and i<=end):
               myball = -1
            else:
                myball = 0
            balls = balls[0:start] + balls[end+1:]
            #print start, end
            return balls,myball
    return balls,myball
if __name__ == '__main__':
#
    # print destroy([1, 2, 3, 4], 4)
    # print destroy([1, 0, 0, 0], 4)
    # print destroy([0, 0, 0, 1], 4)
    # print destroy([0, 0, 0, 0], 4)
    # print destroy([1,0, 0, 0, 0,1,1,1], 8)
    # print destroy([2, 1, 2, 2, 2, 1, 2, 2, 1, 1, 2],11)
    n, k, x = map(int, raw_input().split())
    balls = map(int, raw_input().split())
    maxBalls = 0
    cmax = 0
    originBalls = balls
    for i in xrange(n):

        balls = add_ball(balls, i, k)
        print balls
        cmax = 0
        my_ball_is_there = 1
        while (1):
            new_balls,myball = destroy(balls, len(balls),i)
            if len(new_balls) == len(balls):
                break
            if (my_ball_is_there):
                cmax+=len(balls) - len(new_balls) + myball
                if myball != 0:
                    my_ball_is_there = 0
            balls = new_balls
        maxBalls = max(cmax, maxBalls)
        balls = originBalls
        print balls
    print maxBalls
