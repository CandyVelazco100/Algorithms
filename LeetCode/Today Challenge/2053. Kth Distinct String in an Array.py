2053. Kth Distinct String in an Array
A distinct string is a string that is present only once in an array.

Given an array of strings arr, and an integer k, return the kth distinct string present in arr. 
If there are fewer than k distinct strings, return an empty string "".

Note that the strings are considered in the order in which they appear in the array.

class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        counter = Counter(arr)

        for word in arr:
            if counter[word] == 1:
                k -= 1
                if k == 0:
                    return word
        return ''
