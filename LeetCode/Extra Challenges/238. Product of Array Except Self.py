Given an integer array nums, return an array answer such that answer[i] 
is equal to the product of all the elements of nums except nums[i].

# No optmized time
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = [0] * len(nums)
        for i in range(len(nums)):
            productExcl = 1
            for j in range(len(nums)):
                if i == j:
                    continue
                productExcl = productExcl*nums[j]
            product[i] = productExcl
        return product      

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        prefix = [1] * n
        suffix = [1] * n
        
        for i in range(1, n):
            prefix[i] = prefix[i - 1] * nums[i - 1]
        
        for i in range(n - 2, -1, -1):
            suffix[i] = suffix[i + 1] * nums[i + 1]
        
        answer = [prefix[i] * suffix[i] for i in range(n)]
        
        return answer  
