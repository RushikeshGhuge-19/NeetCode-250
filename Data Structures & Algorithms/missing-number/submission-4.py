class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        exp = n*(n + 1)//2
        curr = sum(nums)
        return exp - curr

        
        