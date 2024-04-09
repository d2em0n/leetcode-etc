class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        answer = True
        change = {5 : 0, 10 : 0, 20: 0}
        for bill in bills:
            change[bill] += 1
            if bill - 5 == 0:
                continue
            elif bill - 5 == 5:
                if change[5] > 0:
                    change[5] -= 1
                else:
                    answer =  False
                    break
            elif bill - 5 == 10:
                if change[10] > 0:
                    change[10] -= 1
                elif change[5] >= 2:
                    change[5] -= 2
                else:
                    answer = False
                    break
            else:
                if change[5] > 0 and change[10] > 0:
                    change[5] -= 1
                    change[10] -= 1
                elif change[5] >= 3:
                    change[5] -= 3
                else:
                    answer = False
                    break
        return answer