class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #stack这里面呢
        #只要是速度小的肯定就可以合并 只要是速度大的 那么就需要入栈？？速度大肯定是一个新的车队
        #肯定是先要排个序吧
        pair=[(p,s) for p,s in zip(position,speed)]
        pair.sort(reverse=True)
        fleet=1

        prevTime=(target-pair[0][0])/pair[0][1]
        for i in range(1,len(pair)):
            curTime=(target-pair[i][0])/pair[i][1]
            if curTime>prevTime:
                fleet+=1
                prevTime=curTime
        return fleet
       

        