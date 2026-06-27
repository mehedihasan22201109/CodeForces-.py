cases = int(input())

for _ in range(cases):
    n, k = map(int, input().split())

    result = 0
    value = 1

    while n >= value:
        people = n // value

        if people > k:
            people = k

        result += people
        n -= people * value

        value *= 2

    print(result)