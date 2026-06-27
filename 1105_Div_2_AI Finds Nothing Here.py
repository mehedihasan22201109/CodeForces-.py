MOD = 998244353

t = int(input())

for _ in range(t):
    rows, cols, scan_rows, scan_cols = map(int, input().split())

    free_cells = 0

    # First (scan_cols - 1) columns are completely free
    free_cells += rows * (scan_cols - 1)

    # In the remaining columns, only the first (scan_rows - 1) rows are free
    remaining_columns = cols - (scan_cols - 1)
    free_cells += remaining_columns * (scan_rows - 1)

    print(pow(2, free_cells, MOD))