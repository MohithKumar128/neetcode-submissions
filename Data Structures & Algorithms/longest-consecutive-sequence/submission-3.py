class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums==[]:
            return 0
        nums = list(set(nums))  # remove duplicates
        nums.sort()

        longest = 1
        current = 1

        for i in range(1, len(nums)):
            if nums[i] - nums[i-1] == 1:
                current += 1
                longest = max(longest, current)
            else:
                current = 1  # reset!

        return longest
        


        