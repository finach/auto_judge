"""
https://leetcode.com/problems/two-sum/

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Constraints:
    * 2 <= nums.length <= 10^4
    * -10^9 <= nums[i] <= 10^9
    * -10^9 <= target <= 10^9
    * Only one valid answer exists.
"""

import pytest
from typing import List


class Solution:
    def twoSum_n2(self, nums: List[int], target: int) -> List[int]:
        """
        Brute-force solution to find two indices whose values sum to the target.

        Time Complexity: O(n^2)
        """
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

    def twoSum_nlogn(self, nums: List[int], target: int) -> List[int]:
        """
        Solution using sorting and two-pointer technique to find two indices whose values sum to the target.

        Time Complexity: O(n log n)
        """
        # Sort nums with original indices
        nums_sort = sorted([(n, i) for i, n in enumerate(nums)])

        # Iterate through the sorted list
        for i in range(len(nums_sort)):
            # Iterate backwards to find the target sum
            for j in range(-1, i - len(nums_sort), -1):
                if nums_sort[i][0] + nums_sort[j][0] == target:
                    return [nums_sort[i][1], nums_sort[j][1]]

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Finds two indices in the list such that their values sum to the target using a dictionary.

        Time Complexity: O(n)
        """
        # Dictionary to store numbers as keys and their indices as values
        mydict = {}

        for i, n in enumerate(nums):
            # Check if the partner (target - current number) is in the dictionary
            if target - n in mydict:
                return [i, mydict[target - n]]
            else:
                mydict[n] = i


# ================ Sample input to test ================
@pytest.mark.parametrize(
    "nums, target, output",
    [
        ([2, 7, 11, 15], 9, [0, 1]),
        ([3, 2, 4], 6, [1, 2]),
        ([3, 3], 6, [0, 1]),
    ],
)
def test_two_sum(nums: List[int], target: int, output: List[int]):
    assert output == sorted(Solution().twoSum(nums, target))
