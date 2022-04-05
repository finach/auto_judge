"""
https://zerojudge.tw/ShowProblem?problemid=f605

Input Description
    市場上有 n 個商品，你也知道這 n 個商品最近 3 天的價格。
    你想要購買近三天價格最高與最低差異至少 d 的所有物品，而購買物品的費用是它近 3 天的價格的平均值，保證這個平均值會是整數。

    給定 n 個物品最近 3 天的價格，以其所設定的 d，輸出總共購買的商品數量以及費用總和。

Output Description
    在一行輸出兩個數字以空格分隔，依序是購買個商品數量以及總共的花費。

Input Example 1
    1 3
    24 27 21

Output Example 1
    1 24

Input Example 2
    3 4
    24 33 42
    51 48 60
    77 77 77

Output Example 2
    2 86
"""


n, d = map(int, input().split())

buy = cost = 0
for i in range(n):
    prizes = [int(x) for x in input().split()]
    if max(prizes) - min(prizes) >= d:
        cost += sum(prizes) // 3
        buy += 1

print(f"{buy} {cost}")
