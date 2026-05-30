from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_map:
                return [num_map[complement], i]
            num_map[num] = i
        return []


if __name__ == "__main__":
    solution = Solution()

    test_nums = [2, 7, 11, 15]
    test_target = 9

    result = solution.twoSum(test_nums, test_target)
    print(result)