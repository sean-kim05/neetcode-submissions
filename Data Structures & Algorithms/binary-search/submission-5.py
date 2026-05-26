class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)- 1
        while l<=r:
            mp = (l+r) // 2
            if nums[mp] > target:
                r = mp - 1
            elif nums[mp] < target:
                l = mp + 1
            else:
                return mp
        return -1

                

