def find_crimson_triples(limit):
    total_ways = 0
    start_divisor = 1

    while start_divisor <= limit:
        same_value = limit // start_divisor
        last_divisor = limit // same_value

        group_size = last_divisor - start_divisor + 1
        total_ways += group_size * (same_value ** 2)

        start_divisor = last_divisor + 1

    return total_ways


test_cases = int(input())

for _ in range(test_cases):
    n = int(input())
    answer = find_crimson_triples(n)
    print(answer)