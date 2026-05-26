class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        find_sum = {}
        for i,n  in enumerate(nums):
            complement = target - n
            if complement in find_sum:
                return [find_sum[complement], i]
            find_sum[n] = i

        