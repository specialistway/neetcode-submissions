class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        #这个哪里是dp呢
        #dp[i]=dp[i-c-1] and s[i-c:] is in wordDict
        #我想把它扩展一下
        #倒着写
        #它肯定需要有一个true
        dp=[False]*(len(s)+1)
        dp[len(s)]=True
        for i in range(len(s)-1,-1,-1):
            for w in wordDict:
                if i+len(w)<=len(s) and s[i:i+len(w)]==w:
                    dp[i]=dp[i+len(w)]
                if dp[i]:
                    break
        return dp[0]

        