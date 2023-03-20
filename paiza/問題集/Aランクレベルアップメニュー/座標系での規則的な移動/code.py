# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
# input_line = input()
Y, X, N = map(int, input().split())

DIRECTION = ["E", "S", "W", "N"]
count = 0
plus_count = 1
frag = True
now_direction = 0

def move(now_direction, X, Y):
    if DIRECTION[now_direction] == "N":
        Y -= 1
    elif DIRECTION[now_direction] == "E":
        X += 1
    elif DIRECTION[now_direction] == "S":
        Y += 1
    elif DIRECTION[now_direction] == "W":
        X -= 1
        
    return (X, Y)
    
for _ in range(N):
    (X, Y) = move(now_direction, X, Y)
    count += 1
    
    if frag and plus_count == count:
        frag = False
        count = 0
        now_direction = (1 + now_direction) % 4
    elif plus_count == count:
        count = 0
        plus_count += 1
        frag = True
        now_direction = (1 + now_direction) % 4
        
        
# 1 E
# 1 S
# elif
# 2 W  2loops
# 2 N  2loops
# elif
# 3 E  3loops
# 3 S  3loops
# elif
# 4 W  4loops
# 4 N  4loops
# fragを用いることで次も同じ回数ループするか、1回足すかを判定している

print(X, Y)

    
    
    
