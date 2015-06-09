class Solution:
    # @param n, an integer
    # @return an integer
    def climbStairs(self, n, k=0, ways=0):
        if n == 0 or n == 1:
            return 1
        dp = [1,2]
        for i in range(2,n):
            s = dp[0] + dp[1]
            dp[0] = dp[1]
            dp[1] = s
        return dp[1] 

for i in range(1,36):
    print Solution().climbStairs(i)
print Solution().climbStairs(2)
print Solution().climbStairs(3)
print Solution().climbStairs(4)
print Solution().climbStairs(10)
print Solution().climbStairs(35)
