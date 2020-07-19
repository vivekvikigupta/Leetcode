class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        opt_arr = []
        sze = len(nums) #calculating size of array
        for i in range(sze):
            index = abs(nums[i]) - 1
            if nums[index] < 0:
                opt_arr.append(abs(nums[i]))
            else:
                nums[index] = -nums[index]
        return opt_arr