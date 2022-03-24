"""
https://zerojudge.tw/ShowProblem?problemid=f579

Input Description
    給兩個整數 a, b 代表你要觀察的商品編號。
    一個正整數 x 表示這位客人將一個編號是 x 的商品放入他的購物車，一個負數 −x 表示這位客人將一個編號是 x 的商品從他的購物車移除。
    現在有 n 位客人的購物車紀錄，你想要統計有幾位客人最後有購買商品 a 與商品 b，一個客人有購買商品 x 表示商品 x 在他的購物車中放入的次數比拿出還多。

    第一行有兩個正整數 a, b (1<=a,b<=100)。
    第二行有一個正整數 n(1<=n<=100)，表示客人的數量。
    接下來有 n 行，第 i 行表示第 i 位客人的購物車紀錄。
    對於每個購物車紀錄包含一連串的整數，最後一個數字必定為 0，表示購物紀錄結尾，其他數字必定為非 0 的整數且絕對值不超過 100，定義同題目敘述。

Output Description
    輸出一個整數，表示有幾位客人同時有購買商品 a 與商品 b。

Input Example 1
    1 8
    5
    1 8 0
    5 6 0
    2 7 0
    8 1 0
    33 22 0

Output Example 1
    2

Input Example 2
    3 9
    2
    3 9 -3 3 9 0
    3 3 -3 -3 9 0

Output Example 2
    1
"""

ans = 0
a, b = map(int, input().split())
n = int(input())

for i in range(n):
    commodities = [int(x) for x in input().split()]
    pa = pb = 0
    for c in commodities:
        if abs(c) == a:
            pa += c
        if abs(c) == b:
            pb += c
    if pa > 0 and pb > 0:
        ans += 1

print(ans)
