class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        total = 0
        remainderMap = {0:-1}

        for i, n in enumerate(nums):
            total += n
            r = total%k
            if r not in remainderMap:
                remainderMap[r] = i
            elif i - remainderMap[r] > 1:
                return True
        return False
        