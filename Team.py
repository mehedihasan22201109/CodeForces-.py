total_problems = int(input())

solvable_problems = 0

for _ in range(total_problems):
    petya, vasya, tonya = map(int, input().split())

    if petya + vasya + tonya >= 2:
        solvable_problems += 1

print(solvable_problems)