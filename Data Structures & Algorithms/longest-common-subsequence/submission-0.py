class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        #都说了是2d的了
        #dp[i][j]表示1的前i个和2的前j个有多少个》？？？
        #f[i][j]=f[i-1][j]+f[i][j-1]
        dp=[[0 for j in range(len(text2)+1)] for i in range(len(text1)+1)]
        for i in range(len(text1)-1,-1,-1):
            for j in range(len(text2)-1,-1,-1):
                if text1[i]==text2[j]:
                    dp[i][j]=1+dp[i+1][j+1]
                else:
                    dp[i][j]=max(dp[i+1][j],dp[i][j+1])
        return dp[0][0]
        