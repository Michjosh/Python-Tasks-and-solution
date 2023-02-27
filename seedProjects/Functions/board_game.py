def create_board(length, width, piece):
    # Initialize the board with default values
    board_array = [[" " for _ in range(width)] for _ in range(length)]

    # Fill in the board with pieces
    for piece in piece:
        row = piece["row"]
        col = piece["col"]
        value = piece["value"]
        print(end='')
        board_array[row][col] = value

    return board_array


pieces = [
    {"row": 0, "col": 0, "value": "X"},
    {"row": 0, "col": 1, "value": "O"},
    {"row": 0, "col": 2, "value": "X"},
    {"row": 1, "col": 0, "value": "X"},
    {"row": 1, "col": 1, "value": "X"},
    {"row": 1, "col": 2, "value": "X"},
    {"row": 2, "col": 0, "value": "X"},
    {"row": 2, "col": 1, "value": "X"},
    {"row": 2, "col": 2, "value": "X"},
]
board = create_board(3, 3, pieces)
print(board)
