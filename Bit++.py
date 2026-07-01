line_count = int(input())

result = 0

for _ in range(line_count):
    expression = input()

    if '+' in expression:
        result += 1
    else:
        result -= 1

print(result)