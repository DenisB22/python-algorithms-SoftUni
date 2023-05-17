def move_down_right(row, col, rows, cols):
    if row >= rows or col >= cols:
        return 0

    if row == rows - 1 and col == cols - 1:
        return 1

    count = 0

    count += move_down_right(row + 1, col, rows, cols)
    count += move_down_right(row, col + 1, rows, cols)

    return count


rows = int(input())
cols = int(input())
print(move_down_right(0, 0, rows, cols))
