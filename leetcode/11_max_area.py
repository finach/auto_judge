"""
https://leetcode.com/problems/container-with-most-water/description/

You are given an integer array height of length n.
There are n vertical lines drawn such that the two endpoints of the i^th line are (i, 0) and (i, height[i]).
Find two lines that together with the x-axis form a container, such that the container contains the most water.
Return the maximum amount of water a container can store.
Notice that you may not slant the container.

Constraints:
    * n == height.length
    * 2 <= n <= 105
    * 0 <= height[i] <= 104
"""

import pytest
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        maximum, left, right = 0, 0, len(height) - 1
        while left < right:
            maximum = max(maximum, min(height[left], height[right]) * (right - left))
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
        return maximum


# ================ Sample input to test ================
@pytest.mark.parametrize(
    "height, output",
    [
        ([1, 8, 6, 2, 5, 4, 8, 3, 7], 49),
        ([1, 1], 1),
    ],
)
def test_maxArea(height: List[int], output: int):
    assert output == Solution().maxArea(height)
