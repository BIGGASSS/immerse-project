grid = [[0, 1, 2, 3, 4],
              [5, 6, 7, 8, 9],
              [10, 11, 12, 13, 14],
              [15, 16, 17, 18, 19],
              [20, 21, 22, 23, 24]]

# Transpose in-place by swapping elements
for i in range(5):
    for j in range(i + 1, 5):  # Only swap upper triangle
        grid[i][j], grid[j][i] = grid[j][i], grid[i][j]

for i in range(5):
    print(grid[i])