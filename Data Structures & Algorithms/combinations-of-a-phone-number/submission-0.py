class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        #这个就完全是一颗树啊哈哈哈
        #不包含1
        #你要先建立一个字典呗
        tele={'2':['a','b','c'],
        '3':['d','e','f'],
        '4':['g','h','i'],
        '5':['j','k','l'],
        '6':['m','n','o'],
        '7':['p','q','r','s'],
        '8':['t','u','v'],
        '9':['w','x','y','z'],
        }
        combination=[]
        res=[]
        def dfs(i):
            if i>=len(digits):
                if len(combination)!=0:
                    res.append(''.join(combination.copy()))
                return
            for letter in tele[digits[i]]:
                combination.append(letter)
                dfs(i+1)
                combination.pop()
        dfs(0)
        return res
        