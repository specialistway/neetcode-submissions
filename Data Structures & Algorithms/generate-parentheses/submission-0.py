class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        #但是你还要判断它是不是合法的
        #对于每一个左括号 都要有一个对应的右括号
        #((()))
        #只要有一个左括号没有匹配上就不行
        #同时还需要一个栈去判断是不是一个合法的遍历
        #为什么不能用栈
        res=[]
        def dfs(op,close,ans):
            if op ==n and close==n:
                res.append(''.join(ans.copy()))
                
            # add open you need to see 
            if op<n:
                ans.append('(')
                dfs(op+1,close,ans)

                ans.pop()
            
            #or add close
            if close<op:
                ans.append(')')
                dfs(op,close+1,ans)
                ans.pop()
        dfs(0,0,[])
        return res
