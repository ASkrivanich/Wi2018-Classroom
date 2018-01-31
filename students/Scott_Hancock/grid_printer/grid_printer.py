def print_grid2(columns = 2, width = 1):
    for i in range(columns + 1):
        main_row_str = '+' + (' -' * width) + ' '
        next_row_str = '|' + ('  ' * width) + ' '
        print((main_row_str * columns) + '+')
        if i < columns:
            for j in range(width):
                print((next_row_str * columns) + '|')
    return

print_grid2(5, 3)
