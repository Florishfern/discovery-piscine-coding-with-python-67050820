def checkmate(board):
    """
    Check if the King is in check on the given chessboard.
    
    Args:
        board: A string representing rows of a chessboard
        
    Returns:
        None, but prints "Success" if King is in check, "Fail" otherwise
    """
    # Parse the board into a 2D list for easier manipulation
    rows = board.strip().split('\n')
    
    # Check if board is a square
    size = len(rows)
    for row in rows:
        if len(row) != size:
            print("Error")
            return
    
    # Find the King's position
    king_pos = None
    for i in range(size):
        for j in range(len(rows[i])):
            if rows[i][j] == 'K':
                king_pos = (i, j)
                break
        if king_pos:
            break
    
    # If no King found, return
    if not king_pos:
        print("Error")
        return
    
    # Check if King is in check
    if is_king_in_check(rows, king_pos):
        print("Success")
    else:
        print("Fail")

def is_king_in_check(board, king_pos):
    """
    Check if the King at the given position is in check.
    
    Args:
        board: A 2D list representing the chessboard
        king_pos: Tuple (row, col) of the King's position
        
    Returns:
        Boolean: True if King is in check, False otherwise
    """
    king_row, king_col = king_pos
    size = len(board)
    
    # Check for Pawns (can capture diagonally)
    pawn_attacks = [(-1, -1), (-1, 1)]  # Pawns attack diagonally from above
    for dr, dc in pawn_attacks:
        r, c = king_row + dr, king_col + dc
        if 0 <= r < size and 0 <= c < size and board[r][c] == 'P':
            return True
    
    # Check for Bishops and diagonal Queen moves
    for dr, dc in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:  # Diagonal directions
        r, c = king_row, king_col
        while True:
            r += dr
            c += dc
            if not (0 <= r < size and 0 <= c < size):
                break
            
            piece = board[r][c]
            if piece == 'B' or piece == 'Q':
                return True
            elif piece != '.':  # Any other piece blocks the line of sight
                break
    
    # Check for Rooks and horizontal/vertical Queen moves
    for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:  # Horizontal/vertical directions
        r, c = king_row, king_col
        while True:
            r += dr
            c += dc
            if not (0 <= r < size and 0 <= c < size):
                break
            
            piece = board[r][c]
            if piece == 'R' or piece == 'Q':
                return True
            elif piece != '.':  # Any other piece blocks the line of sight
                break
    
    return False