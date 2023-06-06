class Solution(object):
    def merge(self, nums1, m, nums2, n):

        i=0
        index=0
        check=0
        for i in range(0,n):
            j=index
            check = 0
            for j in range (index,m+n):
                if check == 0:
                    if nums2[i]<nums1[j]:
                        source = (m+n)-2
                        target = (m+n)-1
                        while(source>=j):
                            nums1[target] = nums1[source]
                            source = source -1
                            target = target -1
                        nums1[target] = nums2[i]
                        index=j+1;
                        break
                    else:
                        if(n-i == (m+n)-j):
                            nums1[j]=nums2[i]
                            check=1
                else:
                    index=j
                    break
                    
        return(nums1)