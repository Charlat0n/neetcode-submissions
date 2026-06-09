class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            check = nums[i]
            for j in range(len(nums)):
                if nums[j] == check and j != i:
                    return True
        return False