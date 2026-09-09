class MyHashSet:
    #维持一个有序的列表就行了 二分排序？？插入 二分排序删除 二分排序查找
    #二分排序的问题

    def __init__(self):
        self.set=[0]*31251
    def getMask(self,key:int)->int:
        return 1<<(key%32)

    def add(self, key: int) -> None:
        self.set[key//32]|=self.getMask(key)

    def remove(self, key: int) -> None:
        if self.contains(key):
            self.set[key//32]^=self.getMask(key)


    def contains(self, key: int) -> bool:
        return self.set[key//32] & self.getMask(key)!=0


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)