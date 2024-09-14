# Table printer
def printTable(table):
    # each column right-justified based on longest string of each list
    # get longest string of each list
    colWidths = []
    colSize = len(table[0])
    rowSize = len(table)

    for x in range(len(table)):
        length = 0
        for y in range(len(table[x])):
            if length < len(table[x][y]):
                length = len(table[x][y])

        colWidths.append(length)


    for col in range(colSize):
        for row in range(rowSize):
            print(table[row][col].rjust(colWidths[row]), end=' ')
        print('\n')

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

printTable(tableData)
