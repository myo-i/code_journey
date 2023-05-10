# https://paiza.jp/works/mondai/a_rank_level_up_problems/a_rank_snake_move_boss

X, Y, N = map(int, input().split())
d = []
for n in range(N):
    d.append(input())

direction = "N"
for l_or_r in d:
    if direction == "N":
        if l_or_r == "L":
            X -= 1
            direction = "W"
        else:
            X += 1
            direction = "E"

    elif direction == "E":
        if l_or_r == "L":
            Y -= 1
            direction = "N"
        else:
            Y += 1
            direction = "S"
            
    elif direction == "S":
        if l_or_r == "L":
            X += 1
            direction = "E"
        else:
            X -= 1
            direction = "W"
            
    elif direction == "W":
        if l_or_r == "L":
            Y += 1
            direction = "S"
        else:
            Y -= 1
            direction = "N"
    print(X,Y)
