t = int(input())

for _ in range(t):
    n, c = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    possible_costs = []

    cur = 0
    for x, y in zip(a, b):
        if x < y:
            break
        cur += x - y
    else:
        possible_costs.append(cur)

    x = sorted(a)
    y = sorted(b)

    good = all(p >= q for p, q in zip(x, y))

    if good:
        dec = 0
        for i in range(n):
            dec += x[i] - y[i]

        possible_costs.append(dec + c)

    if possible_costs:
        print(min(possible_costs))
    else:
        print(-1)