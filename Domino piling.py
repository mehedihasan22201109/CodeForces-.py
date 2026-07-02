board_height, board_width = map(int, input().split())

covered_cells = board_height * board_width

print(covered_cells // 2)