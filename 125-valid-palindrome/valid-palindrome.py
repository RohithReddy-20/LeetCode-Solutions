class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        process = ""
        for char in s:
            if char.isalnum():
                process += char.lower()
        return process == process[::-1]
   
        
       
        