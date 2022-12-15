N, K, P = map(int, input().split())

# 生徒の伸長とイベントを格納
students = list(int(input()) for x in range(N))
events = list(input() for x in range(K))

students.append(int(P))
for event in events:
    if event.startswith("join"):
        splits = event.split()
        students.append(int(splits[1]))
    else:
        students = sorted(students)
        print(students.index(P) + 1)

    
