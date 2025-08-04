class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        decA = int(a,2)
        decB = int(b,2)
        decSum = decA + decB
        binarySum = bin(decSum)
        return binarySum[2:]
        
      