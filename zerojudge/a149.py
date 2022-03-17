"""
https://zerojudge.tw/ShowProblem?problemid=a149

Input Description
    看到 356 就會想要知道 3 * 5 * 6 的值為何。
    一開始有一個數字 T，表示共有幾組測試資料。接下來有 T 個數字 n (0 <= n < 2147483648)。

Output Description
    輸出相乘過後的數字

Input Example 1
    3
    356
    123
    9999

Output Example 1
    90
    6
    6561
"""


times = int(input())
for t in range(times):
    n = int(input())

    # when number is 0
    if n == 0:
        print(0)
        continue

    ans = 1
    while n > 0:
        last = n % 10
        n //= 10
        ans *= last
    print(ans)