"""
https://leetcode.com/problems/remove-duplicates-from-sorted-array/

Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once.
The relative order of the elements should be kept the same. Then return the number of unique elements in nums.
Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:
    * Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially.
      The remaining elements of nums are not important as well as the size of nums.
    * Return k.

Constraints:
    * 1 <= nums.length <= 3 * 10^4
    * -100 <= nums[i] <= 100
    * nums is sorted in non-decreasing order.
"""

import pytest
from typing import List


class Solution:
    def removeDuplicates_n2(self, nums: List[int]) -> int:
        """
        Removes duplicates from a sorted array by popping duplicates and returns the new length.

        Time Complexity: O(n^2)
            repeated use of pop(), which is O(n) for each call, making the overall complexity quadratic.
        """
        left, right = 0, 1
        while right < len(nums):
            if nums[left] == nums[right]:
                nums.pop(left)
                # print(f"{nums=}, {left=}, {right=}")
            else:
                left += 1
                right += 1
        return left + 1

    def removeDuplicates(self, nums: List[int]) -> int:
        """
        Removes duplicates from a sorted array in-place and returns the new length.

        Time Complexity: O(n)
            where n is the length of the array. We iterate through the array once.
        """
        left = 0
        for right in range(1, len(nums)):
            if nums[left] != nums[right]:
                left += 1
                nums[left] = nums[right]
        return left + 1


# ================ Sample input to test ================
@pytest.mark.parametrize(
    "nums, expected_output, expected_nums",
    [
        ([1, 1, 2], 2, [1, 2]),
        ([0, 0, 1, 1, 1, 2, 2, 3, 3, 4], 5, [0, 1, 2, 3, 4]),
        ([0], 1, [0]),
    ],
)
def test_removeDuplicates(nums: List[int], expected_output: int, expected_nums: List[int]):
    assert expected_output == Solution().removeDuplicates(nums)
    assert nums[:expected_output] == expected_nums
