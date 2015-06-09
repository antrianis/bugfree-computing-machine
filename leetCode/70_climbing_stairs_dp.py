class Solution:
    # @param n, an integer
    # @return an integer
    def climbStairs(self, n, k=0, ways=0):
        if n == 1:
            return 1
        if n == 2:
            return 2
        dp = [0] * (n+1)
        dp[0] = 0
        dp[1] = 1
        dp[2] = 2
        for i in range(3,n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n] 

for i in range(1,36):
    print Solution().climbStairs(i)
print Solution().climbStairs(2)
print Solution().climbStairs(3)
print Solution().climbStairs(4)
print Solution().climbStairs(10)
print Solution().climbStairs(35)
