class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort()
        dp=[float("inf")]*(amount+1)
        dp[0]=0
        
        for i in range(1,amount+1):
            for j in coins:
                if i-j>=0:
                    dp[i]=min(dp[i],1+dp[i-j])         
        if dp[amount]!=float("inf"):
            return dp[amount]
        else:
            return -1
        