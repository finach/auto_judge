"""
https://zerojudge.tw/ShowProblem?problemid=g595

Input Description
    有一個農場有寬度為 n 的圍籬, 每個圍籬都有各自的高度 h[1],h[2],⋯,h[n]
    有些圍籬被吹斷了，農場主人要來修補這些圍籬，取斷掉的圍籬位置相鄰左邊和右邊較小的那個高度填上去，問需要多少成本
    題目保證不會有兩個相鄰的吹斷圍籬，而穿斷的圍籬有可能位在邊界

    輸入包含兩行
    第一行有一個正整數 n
    第二行有 n 個以空隔分隔的整數 h[1],h[2],⋯,h[n]

    數字範圍
    3<=n<=100
    0<=h[i]<=100

Output Description
    輸出一個正整數表示新增的圍籬長度總和

Input Example 1
    3
    2 0 4

Output Example 1
    2

Input Example 2
    9
    0 5 3 0 6 4 0 1 0

Output Example 2
    10
"""


n = int(input())
s = [100] + [int(i) for i in input().split()] + [100]

total = 0
for i in range(1, n + 1):
    if s[i] == 0:
        total += min(s[i - 1], s[i + 1])
print(total)
