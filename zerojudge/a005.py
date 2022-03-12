"""
https://zerojudge.tw/ShowProblem?problemid=a005

Input Description
    第一行是數列的數目t（0 <= t <= 20）。 以下每行均包含四個整數，表示數列的前四項。 約定數列的前五項均為不大於105的自然數，等比數列的比值也是自然數。

Input Example
    2
    1 2 3 4
    1 2 4 8

Output Description
    對輸入的每個數列，輸出它的前五項。
    
Output Example
    1 2 3 4 5
    1 2 4 8 16
"""

n = int(input())
for i in range(n):
    s = [int(x) for x in input().split()]
    
    intervel = s[1] - s[0]
    arithmetic = True
    for x in range(1, len(s) - 1):
        if s[x + 1] - s[x] != intervel:
            arithmetic = False
            break

    if arithmetic:
        s.append(s[-1] - s[-2] + s[-1])
    else:
        s.append(s[-1] // s[-2] * s[-1])
    print(*s)