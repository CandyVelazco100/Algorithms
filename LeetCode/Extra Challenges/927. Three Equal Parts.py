You are given an array arr which consists of only zeros and ones, 
divide the array into three non-empty parts such that all of these parts represent the same binary value.
If it is possible, return any [i, j] with i + 1 < j

class Solution:
    def threeEqualParts(self, arr: List[int]) -> List[int]:
        ones = arr.count(1)

        if ones == 0:
            return [0, len(arr)-1]
        if ones % 3 != 0:
            return [-1, -1]
        
        ones_in_number = ones // 3
        start0 = arr.index(1)
        i = start0
        ones = 0

        while ones < ones_in_number:
            if arr[i] == 1:
                ones += 1
            i += 1
        
        l = i - start0
        start1 = arr.index(1, start0 + l)
        start2 = arr.index(1, start1 + l)

        l = len(arr) - start2

        if arr[start0:start0+l] == arr[start1:start1+l] == arr[start2:start2+l]:
            return [start0 + l - 1, start1 + l]
        else:
            return [-1, -1]
