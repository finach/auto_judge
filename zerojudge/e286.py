"""
https://zerojudge.tw/ShowProblem?problemid=e286

Input Description
    單筆輸入
    共有四行數字，代表兩場比賽
    每行有四個數字，代表四局的分數
    第一行代表主隊在第一場比賽中四局的分數
    第二行代表客隊在第一場比賽中四局的分數
    第三行代表主隊在第二場比賽中四局的分數
    第四行代表客隊在第二場比賽中四局的分數
    所有數字都介於 0 ~ 100 之間

Output Description
    對每一場比賽輸出主隊與客隊的比數
    最後輸出兩場比賽的勝敗情況
    如果主隊贏了兩場輸出 "Win"
    如果客隊贏了兩場輸出 "Lose"
    平手則輸出 "Tie"
    保證不會有同分狀況出現，每場都會分出勝負

Input Example 1
    87 87 87 87
    78 78 78 78
    87 87 87 87
    78 78 78 78

Output Example 1
    348:312
    348:312
    Win
"""


scores = [sum([int(s) for s in input().split()]) for i in range(4)]

win = 0
for i in range(0, len(scores), 2):
    print(f'{scores[i]}:{scores[i+1]}')
    if scores[i] > scores[i+1]:
        win += 1

if win == 2:
    print('Win')
elif win == 1:
    print('Tie')
elif win == 0:
    print('Lose')
