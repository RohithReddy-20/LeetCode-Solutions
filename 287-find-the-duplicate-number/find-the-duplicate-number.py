class Solution(object):
    def findDuplicate(self, num):
        """
        :type nums: List[int]
        :rtype: int
        """
        slow = num[0]
        fast = num[0]
        while True:
            slow = num[slow]
            fast = num[num[fast]]
            if slow == fast:
                break
        fast = num[0]
        while slow != fast:
             slow = num[slow]
             fast = num[fast]
        return slow
       


       