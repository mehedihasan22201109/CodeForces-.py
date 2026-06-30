test_case = int(input())

for _ in range(test_case):
    current, target = map(int, input().split())

    answer = "NO"

    if target == current:
        answer = "YES"
    else:
        if current > target:
            if current % target == 0:
                answer = "YES"

    print(answer)