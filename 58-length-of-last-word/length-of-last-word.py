class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        remove = s.strip()
        words = remove.split(' ')
        return len(words[-1])
     
    
        