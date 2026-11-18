class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        #这个跟graph有啥关系呢
        #看这个list是不是字典序排列的
        #我觉得它这个分类有点误导我了
        index_order={c:i for i,c in enumerate(order)}
        for i in range(1,len(words)):
            w1,w2=words[i-1],words[i]
            for j in range(len(w1)):
                if j==len(w2):
                    return False
                if w1[j]!=w2[j]:
                    if index_order[w1[j]]>index_order[w2[j]]:
                        return False
                    #就是判断第一个不同的字母就可以了，后面就不用再判断了
                    break
        return True



        