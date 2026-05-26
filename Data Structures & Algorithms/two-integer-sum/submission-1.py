class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        empty_dic = {}  # Dictionary to store the number and its index
        
        for i in range(len(nums)):
            j = target - nums[i]
            
            if j in empty_dic:
                return [empty_dic[j], i]
            
            empty_dic[nums[i]] = i

