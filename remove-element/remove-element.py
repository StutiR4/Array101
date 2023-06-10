class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        count=0
        limit = len(nums)-1
        i=0
        for i in range(0,len(nums)):
            if(val != nums[i]):
                count = count+1
        
        i=0
        
        while i < limit:
            if(val==nums[i]):
                for x in range(i, limit):
                    nums[x]=nums[x+1]
                limit=limit-1
            else:
                i=i+1
        
        return(count)