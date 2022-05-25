"""
https://zerojudge.tw/ShowProblem?problemid=c015

Input Description
    重複把數字反轉並加上原來的數字，找到回文。
    195 開始的數字
    591
    -----
    786
    687
    -----
    1473
    3741
    -----
    5214
    4125
    -----
    9339 回文出現了

    第1列有一個整數N（0 < N <= 100），代表以下有幾組測試資料。每筆測試資料一列，各有1個整數 P，就是開始的數字。
    每個整數：
        1. 都會有1個答案。
        2. 在1000個相加內都會得到答案。
        3. 產生的迴文不會大於4294967295.

Output Description
    對每一測試資料，請輸出2個數字：得到迴文所需的最少次數的相加，以及該迴文。

Input Example 1
    5
    195
    265
    750
    2
    99

Output Example 1
    4 9339
    5 45254
    3 6666
    1 4
    6 79497
"""


for i in range(int(input())):
    n = int(input())
    count = 0
    while True:
        count += 1
        n += int(str(n)[::-1])
        left_end = len(str(n)) // 2
        right_start = left_end if len(str(n)) % 2 == 0 else left_end + 1
        if str(n)[:left_end] == str(n)[right_start:][::-1]:
            print(f"{count} {n}")
            break
