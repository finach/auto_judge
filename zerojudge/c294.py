"""
https://zerojudge.tw/ShowProblem?problemid=c294

Input Description
    請設計程式以讀入三個線段的長度判斷並輸出此三線段可否構成三角形？若可，判斷 並輸出其所屬三角形類型。
    提示：若a、b、c為三個線段的邊長，且c為最大值，則
        若 a+b <= c，三線段無法構成三角形
        若 a×a+b×b < c×c，三線段構成鈍角三角形 (Obtuse triangle)
        若 a×a+b×b = c×c，,三線段構成直角三角形 (Right triangle)
        若 a×a+b×b > c×c，三線段構成銳角三角形 (Acute triangle)

    輸入僅一行包含三正整數，三正整數皆小於 30,001，兩數之間有一空白。

Output Description
    輸出共有兩行，第一行由小而大印出此三正整數，兩字之間以一個空白格間格，最後 一個數字後不應有空白；第二行輸出三角形的類型：
        若無法構成三角形時輸出「No」；
        若構成鈍角三形時輸出「Obtuse」；
        若直角三形時輸出「Right」；
        若銳角三形時輸出「Acute」。

Input Example 1
    3 4 5

Output Example 1
    3 4 5
    Right

Input Example 2
    101 100 99

Output Example 2
    99 100 101
    Acute

Input Example 3
    10 10 100

Output Example 3
    10 10 100
    No
"""

nums = [int(x) for x in input().split()]
nums.sort()
print(*nums)

a, b, c = nums[0], nums[1], nums[2]

if a + b <= c or a == 0 or b == 0 or c == 0:
    print('No')
elif a * a + b * b < c * c:
    print('Obtuse')
elif a * a + b * b == c * c:
    print('Right')
elif a * a + b * b > c * c:
    print('Acute')
