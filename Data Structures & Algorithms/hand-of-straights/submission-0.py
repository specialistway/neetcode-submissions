from collections import Counter
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand)%groupSize !=0:
            return False
        hand_map=Counter(hand)
        sorted_keys=sorted(hand_map.keys())#对字典排序 需要用SORTED
        for key in sorted_keys:
            if hand_map[key]:
                count=hand_map[key]
                for i in range(groupSize):
                    if hand_map[key+i]<count:
                        #key是牌面数字
                        return False
                    hand_map[key+i]-=count
        return True



