class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        map = {")": "(", "}": "{", "]": "["}
        for char in s:
            if char in map.values():
                stack.append(char)
            elif char in map.keys():
                if not stack or map[char] != stack.pop():
                    return False
            else:
                return False
        return not stack

  
        
        