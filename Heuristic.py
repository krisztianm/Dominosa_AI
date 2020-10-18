def Heuristic(node, operators):
    row = node.state.size + 1
    column = node.state.size + 2
    choices = {}  # szótár: kulcsa a dominó elem, értéke pedig a koordináta
    for tile in node.state.TILES:
        choices[tuple(tile)] = None
    grid = node.state.GRID
    board = node.state.BOARD

    '''
    tile = tuple([grid[i][j], grid[i][j + 1]])              # az elem
    reversed_tile = tuple([grid[i][j + 1], grid[i][j]])     # az elem fordítottja
    if tile in choices.keys():                              
        if (tile, None) in choices.items():                 # még nem találtunk megfelelő pozíciót az elemek elhelyezésére
            choices[tile] = [[i, j], [i, j + 1]]
            choices[reversed_tile] = [[i, j + 1], [i, j]]
        else:                                               # már találtunk megfelelő poziciót, ezért kivesszük az elemeket
            choices.pop(tile)                               # mivel nem lehet egyértelműen lehelyezni őket
            choices.pop(reversed_tile)
    '''

    i = 0
    while i < row:
        j = 0
        while j < column:
            if i == row - 1 and j == column - 1:
                break
            if board[i][j] != '-':
                j += 1
                continue
            if j == column - 1:
                if operators.isApplicableVertical(node.state, i, j):
                    tile = tuple([grid[i][j], grid[i + 1][j]])
                    reversed_tile = tuple([grid[i + 1][j], grid[i][j]])
                    if tile in choices.keys():
                        if (tile, None) in choices.items():
                            choices[tile] = [[i, j], [i + 1, j]]
                            choices[reversed_tile] = [[i + 1, j], [i, j]]
                        else:
                            choices.pop(tile)
                            if tile != reversed_tile:
                                choices.pop(reversed_tile)
                j += 1
                continue
            if i == row - 1:
                if operators.isApplicableHorizontal(node.state, i, j):
                    tile = tuple([grid[i][j], grid[i][j + 1]])
                    reversed_tile = tuple([grid[i][j + 1], grid[i][j]])
                    if tile in choices.keys():
                        if (tile, None) in choices.items():
                            choices[tile] = [[i, j], [i, j + 1]]
                            choices[reversed_tile] = [[i, j + 1], [i, j]]
                        else:
                            choices.pop(tile)
                            if tile != reversed_tile:
                                choices.pop(reversed_tile)
                j += 1
                continue
            if operators.isApplicableHorizontal(node.state, i, j):
                tile = tuple([grid[i][j], grid[i][j + 1]])
                reversed_tile = tuple([grid[i][j + 1], grid[i][j]])
                if tile in choices.keys():
                    if (tile, None) in choices.items():
                        choices[tile] = [[i, j], [i, j + 1]]
                        choices[reversed_tile] = [[i, j + 1], [i, j]]
                    else:
                        choices.pop(tile)
                        if tile != reversed_tile:
                            choices.pop(reversed_tile)
            if operators.isApplicableVertical(node.state, i, j):
                tile = tuple([grid[i][j], grid[i + 1][j]])
                reversed_tile = tuple([grid[i + 1][j], grid[i][j]])
                if tile in choices.keys():
                    if (tile, None) in choices.items():
                        choices[tile] = [[i, j], [i + 1, j]]
                        choices[reversed_tile] = [[i + 1, j], [i, j]]
                    else:
                        choices.pop(tile)
                        if tile != reversed_tile:
                            choices.pop(reversed_tile)
            j += 1
        i += 1

    # print(choices)

    for tile in choices.keys():
        first_coord = choices[tile][0]
        x1 = first_coord[0]
        y1 = first_coord[1]
        second_coord = choices[tile][1]
        x2 = second_coord[0]
        y2 = second_coord[1]

        if board[x1][y1] != '-' and board[x2][y2] != '-': # valóban üresek az adott cellák
            continue

        if x1 == x2:  # a koordináták egy sorban helyezkednek el
            if y1 > y2:
                board[x1][y1] = 'L'
                board[x2][y2] = 'R'
            else:
                board[x1][y1] = 'R'
                board[x2][y2] = 'L'
        if y1 == y2:  # a koordináták egy oszlopban helyezkednek el
            if x1 > x2:
                board[x1][y1] = 'U'
                board[x2][y2] = 'D'
            else:
                board[x1][y1] = 'D'
                board[x2][y2] = 'U'
        node.state.popTile(tile[0], tile[1])

    node.state.BOARD = board

    return node