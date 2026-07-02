target_row = 2
target_col = 2

for current_row in range(5):
    values = list(map(int, input().split()))

    if 1 in values:
        current_col = values.index(1)
        print(abs(current_row - target_row) + abs(current_col - target_col))
        break