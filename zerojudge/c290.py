"""
https://zerojudge.tw/ShowProblem?problemid=c290

Input Description
    將一個十進位正整數的奇數位數的和稱為A，偶數位數的和稱為B，則A與B的絕對差值|A-B| 稱為這個正整數的秘密差。
    例如： 263541 的奇數位和 A = 6+5+1 =12，偶數位的和 B = 2+3+4 = 9，所以 263541 的秘密差是 |12-9|= 3。
    給定一個十進位正整數X，請找出X的秘密差。

    輸入為一行含有一個十進位表示法的正整數X，之後是一個換行字元。

Output Description
    請輸出 X的秘密差 Y(以十進位表示法輸出 )，以換行字元結尾 。

Input Example 1
    263541

Output Example 1
    3

Input Example 2
    131

Output Example 2
    1
"""

num = int(input())

A, B = 0, 0
count = 1
while num > 0:
    n = num % 10
    num //= 10

    if count % 2 != 0:
        A += n
    else:
        B += n
    count += 1

print(abs(A-B))
