"""
https://zerojudge.tw/ShowProblem?problemid=a024

Input Description
    輸入包含兩個整數，以空白鍵隔開，兩個整數均大於 0, 小於2^31

Output Description
    輸出兩個整數的最大公因數（GCD）
    
Input Example 1
    12 15
Output Example 1
    3

Input Example 2
    1 100
Output Example 2
    1
"""

x, y = map(int, input().split())

"""
Solution
    y = mx + r
    gcd(x, y) = gcd(x, r), when r = 0, gcd is x
"""
if x > y:
    x, y = y, x

while x > 0:
    r = y % x
    y, x = x, r
print(y)

# TLE, time limit exceeded
# ans = max(x, y)

# while ans > 1:
#     if x % ans == 0 and y % ans == 0:
#         break
#     ans -= 1
# print(ans)