#还得记录一下编号
class TrieNode:
    def __init__(self) -> None:
        self.children={}
        self.isLeaf=-1
class Trie:
    def __init__(self) -> None:
        self.root=TrieNode()
    def addWord(self,word,id):
        curr=self.root
        for c in word:
            if c not in curr.children:
                curr.children[c]=TrieNode()
            curr=curr.children[c]
        curr.isLeaf=id

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        #Trie+dfs
        trie=Trie()
        for i,w in enumerate(words):
            trie.addWord(w,i)
        n,m=len(board),len(board[0])
        res=[]
        visit=set()
        dx,dy=[-1,0,1,0],[0,1,0,-1]
        def dfs(x,y,node):
            if node.isLeaf!=-1:
                res.append(words[node.isLeaf])
                node.isLeaf=-1
            #x,y一定是已经走过了啊
            for i in range(4):
                new_x,new_y=x+dx[i],y+dy[i]
                if new_x<0 or new_x>=n or new_y<0 or new_y>=m or (new_x,new_y) in visit or board[new_x][new_y] not in node.children:
                    continue
                visit.add((new_x,new_y))
                dfs(new_x,new_y,node.children[board[new_x][new_y]])
                visit.remove((new_x,new_y))
            
           
        for i in range(n):
            for j in range(m):
                if board[i][j] in trie.root.children:
                    visit.add((i,j))
                    dfs(i,j,trie.root.children[board[i][j]])
                    visit.remove((i,j))
        return res


        