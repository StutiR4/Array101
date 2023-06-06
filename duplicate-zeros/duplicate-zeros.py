class Solution(object):
    def duplicateZeros(self, arr):

        i=0
        while i < len(arr):
            if arr[i] == 0:
                source = len(arr)-2
                target = len(arr)-1
                while (source>i):
                    arr[target] = arr[source]
                    target = target-1
                    source = source-1
                arr[target] = 0
                i = i+1
            i=i+1
                    
        return (arr)