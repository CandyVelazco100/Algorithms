1460. Make Two Arrays Equal by Reversing Subarrays
You are given two integer arrays of equal length target and arr. In one step, you can select any non-empty subarray of arr and reverse it. You are allowed to make any number of steps.

Return true if you can make arr equal to target or false otherwise.

class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        nTarget = len(target)
        nArr = len(arr)

        if(nTarget != nArr):
            return False
        
        target.sort()
        arr.sort()

        for i in range(nTarget):
            if(target[i] != arr[i]):
                return False
        return True
