from checkmate import checkmate
def main():
    board1 = """\
R.K.
....
....
....\
"""
    print("Example 1 (King in check from Rook):")
    checkmate(board1)
    
    board2 = """\
....
.K..
..B.
....\
"""
    print("\nExample 2 (King in check from Bishop):")
    checkmate(board2)

    board3 = """\
Q...
.K..
....
....\
"""
    print("\nExample 3 (King in check from Queen):")
    checkmate(board3)
    
    board4 = """\
....
PK..
....
....\
"""
    print("\nExample 4 (King in check from Pawn):")
    checkmate(board4)
    
    board5 = """\
....
.K..
.R..
....\
"""
    print("\nExample 5 (King in check from Rook vertically):")
    checkmate(board5)
 
    board6 = """\
R...
.K..
..P.
....\
"""
    print("\nExample 6 (Example from PDF document):")
    checkmate(board6)

if __name__ == "__main__":
    main()