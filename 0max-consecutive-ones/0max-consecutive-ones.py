class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        maxcount = 0
        for i in range (0,len(nums)):
            if nums[i] == 1:
                count = count + 1
            else:
                if maxcount < count:
                    maxcount = count
                count = 0
            if maxcount < count:
                maxcount = count
                    
        return maxcount