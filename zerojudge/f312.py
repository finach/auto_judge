"""
https://zerojudge.tw/ShowProblem?problemid=f312

Input Description
    有一個公司有 n 個員工，還有兩個工廠。如果工廠一與工廠二分別有 X1 與 X2 個員工，兩個工廠的收益 Y1,Y2 分別會是
        Y1=A1×X1^2 + B1×X1 + C1
        Y2=A2×X2^2 + B2×X2 + C2
    請你考慮所有分配員工的方式，找出收益最大的組合，輸出最大收益。
    注意，每個員工皆需分配到其中一個工廠。

    第一行有三個整數 A1,B1,C1
    第二行有三個整數 A2,B2,C2
    第三行有一個正整數 n (1≤n≤100)

Output Description
    輸出最大收益

Input Example 1
    2 -1 3
    4 -5 2
    2

Output Example 1
    11
"""
import sys

a1, b1, c1 = map(int, input().split())
a2, b2, c2 = map(int, input().split())
n = int(input())

ans = -sys.maxsize - 1

for x1 in range(n+1):
    x2 = n - x1
    y1 = (a1 * x1 * x1) + (b1 * x1) + c1
    y2 = (a2 * x2 * x2) + (b2 * x2) + c2

    ans = max(ans, y1+y2)

print(ans)
