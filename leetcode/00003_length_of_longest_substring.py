"""
https://leetcode.com/problems/longest-substring-without-repeating-characters/

Given a string s, find the length of the longest substring without repeating characters.

Constraints:
    * 0 <= s.length <= 5 * 10^4
    * s consists of English letters, digits, symbols and spaces.
"""

import pytest
from collections import defaultdict


class Solution:
    def lengthOfLongestSubstring_n3(self, s: str) -> int:
        """
        This solution uses a brute-force approach to find the longest substring without repeating characters.
        It checks each possible substring by iterating through the string and ensuring no characters repeat.

        Time Complexity: O(n^3)
            Outer Loop (i): Runs n times → O(n).
            Inner Loop (j): For each i, runs up to n times → O(n).
                in Check: The in operation on sub_str (up to length n) → O(n).
        """
        longest = 0
        for i in range(len(s)):
            sub_str = s[i]
            sub_str_len = 1
            for j in range(i + 1, len(s)):
                if s[j] in sub_str:
                    break
                sub_str += s[j]
                sub_str_len += 1
            longest = sub_str_len if sub_str_len > longest else longest
        return longest

    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Uses the sliding window to find the length of the longest substring without repeating characters.

        Time Complexity: O(n)
            where n is the length of the string. Each character is visited at most twice by the 'left' and 'right' pointers.
        """
        longest, left = 0, 0
        cnt = defaultdict(int)  # counter of characters
        for right in range(len(s)):
            while cnt[s[right]]:  # if current character is exist
                cnt[s[left]] -= 1  # shrink the window from the left
                left += 1
                # print(f"duplicate {left=} {right=} {cnt=}")
            cnt[s[right]] += 1  # expand the window
            # print(f"longest {left=} {right=}")
            longest = max(longest, (right - left + 1))
        return longest


# ================ Sample input to test ================
@pytest.mark.parametrize(
    "s, output",
    [
        ("abcabcbb", 3),
        ("bbbbb", 1),
        ("pwwkew", 3),
        ("", 0),
        ("?", 1),
    ],
)
def test_lengthOfLongestSubstring(s: str, output: int):
    assert output == Solution().lengthOfLongestSubstring(s)
