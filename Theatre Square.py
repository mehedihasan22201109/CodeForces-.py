ground_length, ground_width, tile_edge = map(int, input().split())

tiles_along_length = (ground_length + tile_edge - 1) // tile_edge
tiles_along_width = (ground_width + tile_edge - 1) // tile_edge

print(tiles_along_length * tiles_along_width)