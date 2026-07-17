class NumArray:

    def __init__(self, nums: List[int]):
        self.prefixSum = []
        curr = 0 
        for n in nums:
            curr +=n 
            self.prefixSum.append(curr)

    def sumRange(self, left: int, right: int) -> int:
        r = self.prefixSum[right]
        l = self.prefixSum[left - 1] if left > 0 else 0
        return r - l 



# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)