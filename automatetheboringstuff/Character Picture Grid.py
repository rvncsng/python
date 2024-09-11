# Character Picture Grid
grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

result = ''
xLength = len(grid)
yLength = len(grid[0]) #assuming number of columns in each list is equal

for y in range(yLength):
    for x in range(xLength):
        result += grid[x][y]
        if x==xLength-1:
            result += '\n'

print(result)
