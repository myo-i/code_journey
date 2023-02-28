N = input()
K = list(map(int, input().split()))

K = sorted(K)

del K[0:int(N)]
del K[-int(N):]

print(sum(K)/len(K))

# https://atcoder.jp/contests/abc291/tasks/abc291_b