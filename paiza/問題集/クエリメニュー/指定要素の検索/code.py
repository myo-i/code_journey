N, Q = map(int, input().split())
A = [int(input()) for x in range(N)]
K = [int(input()) for x in range(Q)]
for search in K:
    if search in A:
        print("YES")
    else:
        print("NO")


# 入力が98765 100000のような巨大な数値の場合、上記のロジックではタイムアウトする
# 処理が98765回分多くなるため
N, Q = map(int, input().split())
A = {int(input()) for _ in range(N)}

for _ in range(Q):
    k = int(input())
    if k in A:
        print("YES")
    else:
        print("NO")