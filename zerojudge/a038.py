"""
https://zerojudge.tw/ShowProblem?problemid=a038

Input Description
    輸入一行包含一個整數，且不超過2^31

Output Description
    輸出翻轉過後的數字

Input Example 1
    12345
Output Example 1
    54321

Input Example 2
    5050
Output Example 2
    505
"""

i = int(input())
ans = 0

while i > 0:
    last = i % 10
    i //= 10
    ans = ans * 10 + last

print(ans)
