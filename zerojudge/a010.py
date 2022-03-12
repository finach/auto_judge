"""
https://zerojudge.tw/ShowProblem?problemid=a010

Input Description
    輸入共一行。每行包含一個整數，符合 大於1 且 小於等於 100000000

Output Description
    針對每一行輸入整數輸出一個因數分解字串
    
Input Example 1
    20
Output Example 1
    2^2 * 5

Input Example 2
    17
Output Example 2
    17

Input Example 3
    999997
Output Example 3
    757 * 1321
"""

n = int(input())
i = 2
ans = {}
while n > 1:  # input will greater than 1
    if n % i == 0:
        if i in ans:
            ans[i] +=1
        else:
            ans[i]=1
        n = n // i
    else:
        i += 1

# format the output
ans = sorted(ans.items())
ans_string = ''
first = True
for i in ans:
    if not first:
        ans_string += f' * '
    if i[1] != 1:
        ans_string += f'{i[0]}^{i[1]}'
    else:
        ans_string += f'{i[0]}'
    first = False

print(ans_string)