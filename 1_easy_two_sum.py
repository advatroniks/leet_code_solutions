from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        for idx, number in enumerate(nums):
            if number in hash_map:
                return [hash_map[number], idx]
            else:
                desire = target - number
                hash_map[desire] = idx


sol = Solution()
