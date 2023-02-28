from typing import Dict

N = input()

arr = [0, 0]
dictionary = {}
for i in list(input()):
    pair = str(arr[0]) + str(arr[1])
    dictionary[pair] = 0
    match i:
        case "R":
            arr[0] = arr[0] + 1
        case "L":
            arr[0] = arr[0] - 1    
        case "U":
            arr[1] = arr[1] + 1    
        case "D":
            arr[1] = arr[1] - 1
    
if len(dictionary) != int(N):
    print("Yes")
else:
    print("No")
    
# カウンターを用いれば座標の重複が出た時点で処理を停止できる
# https://atcoder.jp/contests/abc291/tasks/abc291_c