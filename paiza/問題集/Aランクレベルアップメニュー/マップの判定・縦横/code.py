# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
H, W = map(int, input().split())
data = []
for num in range(H):
    data.append(input())
for listIndex in range(H):
    for strIndex in range(W):
        if 0 < listIndex < H-1:
            if 0 < strIndex < W-1:
                if(data[listIndex-1][strIndex] == "#" and data[listIndex][strIndex-1] == "#" and data[listIndex][strIndex+1] == "#" and data[listIndex+1][strIndex] == "#"):
                    print(listIndex, strIndex)
            elif strIndex == 0:
                if(data[listIndex-1][strIndex] == "#" and data[listIndex+1][strIndex] == "#" and data[listIndex][strIndex+1] == "#"):
                    print(listIndex, strIndex)
            elif strIndex == W-1:
                if(data[listIndex-1][strIndex] == "#" and data[listIndex+1][strIndex] == "#" and data[listIndex][strIndex-1] == "#"):
                    print(listIndex, strIndex)
        elif listIndex == 0:
            if 0 < strIndex < W-1:
                if(data[0][strIndex-1] == "#" and data[1][strIndex] == "#" and data[0][strIndex+1] == "#"):
                    print(listIndex, strIndex)
            elif strIndex == 0:
                if(data[0][strIndex+1] == "#" and data[1][strIndex] == "#"):
                    print(listIndex, strIndex)
            elif strIndex == W-1:
                if(data[0][strIndex-1] == "#" and data[1][strIndex] == "#"):
                    print(listIndex, strIndex)
        elif listIndex == H-1:
            if 0 < strIndex < W-1:
                if(data[H-1][strIndex-1] == "#" and data[H-2][strIndex] == "#" and data[H-1][strIndex+1] == "#"):
                    print(listIndex, strIndex)
            elif strIndex == 0:
                if(data[H-1][strIndex+1] == "#" and data[H-2][strIndex] == "#"):
                    print(listIndex, strIndex)
            elif strIndex == W-1:
                if(data[H-1][strIndex-1] == "#" and data[H-2][strIndex] == "#"):
                    print(listIndex, strIndex)
            
            
        
# print(data)