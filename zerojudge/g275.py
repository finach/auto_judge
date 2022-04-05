"""
https://zerojudge.tw/ShowProblem?problemid=g275

Input Description
    把平聲標記為0，而仄聲標記為1
    七言對聯有三個限制：
    A: 二四不同二六同：每一句第二、四個字必須不同平仄，而第二、六個字必須相同平仄
    B: 仄起平收：第一句的結尾必須為仄聲，第二句的結尾必須為平聲
    C: 上下相對：第一、二句的第二、四、六個字平仄必須不同

    輸入一個正整數 n (1<=n<=30) 代表對聯數量，接下來有 2n 行，每行有 7 個數字，數字不是 0 就是 1

Output Description
    對於每個對聯，輸出一行表示它違反了哪些規則，若三個規則都遵守則輸出 None

Input Example 1
    1
    1 1 0 0 0 1 1
    1 0 0 0 1 1 0

Output Example 1
    AC

Input Example 2
    1
    0 1 1 0 1 1 1
    1 0 1 1 0 0 0

Output Example 2
    None

Input Example 3
    2
    0 1 1 0 0 0 1
    1 0 1 1 0 1 1
    0 1 0 0 0 0 1
    0 0 0 0 0 1 1

Output Example 3
    AB
    ABC
"""


n = int(input())

for i in range(n):
    s1 = [int(x) for x in input().split()]
    s2 = [int(x) for x in input().split()]

    flag = True
    # A: 二四不同二六同：每一句第二、四個字必須不同平仄，而第二、六個字必須相同平仄
    if not (s1[1] != s1[3] and s1[1] == s1[5] and s2[1] != s2[3] and s2[1] == s2[5]):
        print("A", end="")
        flag = False
    # B: 仄起平收：第一句的結尾必須為仄聲，第二句的結尾必須為平聲
    if not (s1[6] == 1 and s2[6] == 0):
        print("B", end="")
        flag = False
    # C: 上下相對：第一、二句的第二、四、六個字平仄必須不同
    if not (s1[1] != s2[1] and s1[3] != s2[3] and s1[5] != s2[5]):
        print("C", end="")
        flag = False
    if flag:
        print("None")
    print("")
