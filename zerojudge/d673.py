"""
https://zerojudge.tw/ShowProblem?problemid=d673

Input Description
    判斷是否有足夠的題目。如果某個題目是在 X 月出的，該題目必須在 X+1 月或其後的月份才能使用。

    每筆測資的第一行有一個整數 S (0≤S≤100)，表示年初已有的庫存題目數量。
    第二行有 12 個以空白隔開的整數，依序表示一到十二月每個月所出的題目數量。
    第三行也有 12 個以空白隔開的整數，依序表示每個月比賽所需要的題目數量。
    這些整數會介於 0 到 20 之間 (含)。負數代表輸入的結束。

Output Description
    對於每筆測資，印出一行 "Case X:"，X 代表測資編號。
    然後印出 12 行，如果 i 月 (1≤i≤12) 有足夠的題目，則在第 i 行印出 "No problem! :D" (沒有問題)，否則印出 "No problem. :(" (沒有題目)。

Input Example 1
    5
    3 0 3 5 8 2 1 0 3 5 6 9
    0 0 10 2 6 4 1 0 1 1 2 2
    -1

Output Example 1
    Case 1:
    No problem! :D
    No problem! :D
    No problem. :(
    No problem! :D
    No problem! :D
    No problem! :D
    No problem! :D
    No problem! :D
    No problem! :D
    No problem! :D
    No problem! :D
    No problem! :D
"""

for i in range(1, 100):
    cases = int(input())
    if cases < 0:
        break
    print(f"Case {i}:")
    monthly_input = [int(x) for x in input().split()]
    monthly_need = [int(x) for x in input().split()]
    for j in range(len(monthly_need)):
        if cases >= monthly_need[j]:
            print("No problem! :D")
            cases -= monthly_need[j]
        else:
            print("No problem. :(")
        cases += monthly_input[j]

