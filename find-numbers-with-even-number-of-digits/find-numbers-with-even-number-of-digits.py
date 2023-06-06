class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        digitcount=0
        num=0
        numeven=0
        for i in range (0,len(nums)):
            digitcount=0
            num = nums[i]
            while num != 0:
                num = int(num/10)
                digitcount = digitcount+1
            if digitcount%2 == 0:
                numeven = numeven+1
        return (numeven)