class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order_index={c:i for i,c in enumerate(order)}
        for i in range(1,len(words)):
            w1=words[i-1]
            w2=words[i]
            #如果说前面的比后面的长那也不对
            for j in range(len(w1)):
                if j==len(w2):
                    return False
                if order_index[w1[j]]< order_index[w2[j]]:
                    break
                elif order_index[w1[j]]>order_index[w2[j]]:
                    return False
        return True
        