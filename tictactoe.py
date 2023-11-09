def check_win(board, player):
    # Check for horizontal wins
    for i in range(3):
        if all(board[i][j] == player for j in range(3)):
            return True

    # Check for vertical wins
    for j in range(3):
        if all(board[i][j] == player for i in range(3)):
            return True

    # Check for diagonal wins
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2-i] == player for i in range(3)):
        return True

    # No win
    return False


def minimax(board, depth, maximizing_player):
    # Check for terminal states
    if check_win(board, 'X'):
        return -10
    if check_win(board, 'O'):
        return 10
    if all(all(cell != ' ' for cell in row) for row in board):
        return 0

    # Evaluate the current state for the maximizing player
    if maximizing_player:
        score = -float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    new_board = copy.deepcopy(board)
                    new_board[i][j] = 'X'
                    new_score = minimax(new_board, depth + 1, False)
                    score = max(score, new_score)

        return score

    # Evaluate the current state for the minimizing player
    else:
        score = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    new_board = copy.deepcopy(board)
                    new_board[i][j] = 'O'
                    new_score = minimax(new_board, depth + 1, True)
                    score = min(score, new_score)

        return score


def find_best_move(board):
    best_move = None
    best_score = -float('inf')

    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                new_board = copy.deepcopy(board)
                new_board[i][j] = 'X'
                score = minimax(new_board, 0, False)
                if score > best_score:
                    best_score = score
                    best_move = (i, j)

    return best_move


def print_board(board):
    for row in board:
        for cell in row:
            print(cell, end=' ')
        print()


def play_game():
    board = [[' ', ' ', ' '],
             [' ', ' ', ' '],
             [' ', ' ', ' ']]

    current_player = 'X'
    while True:
        # Display the board
        print_board(board)

        # Make a move
        if current_player == 'X':
            move = find_best_move(board)
        else:
            move = input("Enter your move (row,col): ")
            move = (int(move.split(',')[0]), int(move.split(',')[1]))

        # Check for valid move
        if board[move[0]][move[1]] != ' ':
            raise Exception("Invalid move")

        # Make the move
        board[move[0]][move[1]] = current_player

        # Check for win
        if check_win(board, current_player):
            print(f"Player {current_player} wins!")
            break

        # Switch players
        current_player = 'O' if current_player == 'X' else 'X'


if __name__ == "__main__":
    play_game()
