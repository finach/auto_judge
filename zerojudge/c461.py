"""
https://zerojudge.tw/ShowProblem?problemid=c461

Input Description
    輸入只有一行，共三個整數值，整數間以一個空白隔開。
    第一個整數代表 a，第二個整數代表 b，這兩數均為非負的整數。
    第三個整數代表二元運算的結果，只會是 0 或 1。

Output Description
    輸出可能得到指定結果的運算，若有多個，輸出順序為AND、OR、XOR，每個可能的運算單獨輸出一行，每行結尾皆有換行。
    若不可能得到指定結果，輸出IMPOSSIBLE。（注意輸出時所有英文字母均為大寫字母。）

Input Example 1
    0 0 0

Output Example 1
    AND
    OR
    XOR

Input Example 2
    1 1 1

Output Example 2
    AND
    OR

Input Example 3
    3 0 1

Output Example 3
    OR
    XOR

Input Example 4
    0 0 1

Output Example 4
    IMPOSSIBLE
"""

nums = [int(x) for x in input().split()]
a = True if nums[0] != 0 else False
b = True if nums[1] != 0 else False
c = True if nums[2] != 0 else False

impossible = True
if (a and b) == c:
    print('AND')
    impossible = False
if (a or b) == c:
    print('OR')
    impossible = False
if ((a and (not b)) or ((not a) and b)) == c:
    print('XOR')
    impossible = False

if impossible:
    print('IMPOSSIBLE')
