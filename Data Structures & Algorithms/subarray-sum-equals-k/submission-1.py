class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixSum = 0
        result = 0 
        prefixCount = {0:1}

        for num in nums:
            prefixSum += num
            if prefixSum - k in prefixCount:
                result += prefixCount[prefixSum - k]
            prefixCount[prefixSum] = prefixCount.get(prefixSum,0) +1
        return result
        
        