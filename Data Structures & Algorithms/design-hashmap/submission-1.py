class MyHashMap:
    #字典能用吗 set能用吗
    #应该是只有数组能用
    #那还是32250个吗？？不行吧 它需要记录下数组的 hash set只需要记录下存在不存在
    #就是立马要哈希索引到嘿嘿

    def __init__(self):
        self.hashMap=[-1]*1000001

    def put(self, key: int, value: int) -> None:
        self.hashMap[key]=value

    def get(self, key: int) -> int:
        return self.hashMap[key]

    def remove(self, key: int) -> None:
        self.hashMap[key]=-1


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)