class ListNode:
    def __init__(self,key,val):
        self.key=key
        self.val=val
        self.freq=1
        self.prev=None
        self.next=None

class LinkedList:
    def __init__(self):
        self.left=ListNode(0,0)
        self.right=ListNode(0,0)
        self.left.next=self.right
        self.right.prev=self.left
        self.size=0


    def length(self):
        return self.size
    def pushRight(self,node):
        #把nodepush到当前list的右边去
        prev=self.right.prev
        prev.next=node
        node.prev=prev
        node.next=self.right
        self.right.prev=node
        self.size+=1
    def pop(self,node):
        Prev,Next=node.prev,node.next
        Prev.next=Next
        Next.prev=Prev
        node.prev=None
        node.next=None
        self.size-=1
    def popLeft(self):
        if self.length()==0:
            return None
        node=self.left.next
        self.pop(node)
        return node

#pop的时候已经知道node了 但是popleft的时候不知道node
class LFUCache:
    #得用2种数据结构才行
    def __init__(self, capacity: int):
        self.cap=capacity
        self.lfuCnt=0
        self.nodeMap={}
        self.listMap=defaultdict(LinkedList)

    def counter(self,node):
        #修改一个node的位置并且更新lfucnt
        cnt=node.freq
        self.listMap[cnt].pop(node)
        if cnt==self.lfuCnt and self.listMap[cnt].length()==0:
            self.lfuCnt+=1
        node.freq+=1
        self.listMap[node.freq].pushRight(node)
       
    def get(self, key: int) -> int:#找到并且改频率
        if key not in self.nodeMap:
            return -1
        node=self.nodeMap[key]
        self.counter(node)
        return node.val
        
    def put(self, key: int, value: int) -> None:
        if self.cap==0:
            return
        if key in self.nodeMap:
            node=self.nodeMap[key]
            node.val=value
            self.counter(node)
            return
        if len(self.nodeMap)==self.cap:
            node=self.listMap[self.lfuCnt].popLeft()
            self.nodeMap.pop(node.key)
        node=ListNode(key,value)
        self.nodeMap[key]=node
        self.listMap[1].pushRight(node)
        self.lfuCnt=1



# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)