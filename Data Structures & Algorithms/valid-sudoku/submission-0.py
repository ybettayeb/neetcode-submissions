class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in range(9):
            seenRow = set()
            for j in range(9):
                if board[row][j] == ".":
                    continue
                if board[row][j] in seenRow:
                    return False
                seenRow.add(board[row][j])
        for col in range(9):
            seenCol = set()
            for i in range(9):
                if board[i][col] == ".":
                    continue
                if board[i][col] in seenCol:
                    return False
                seenCol.add(board[i][col])
        

        for Square in range(9):
            seenBox = set()
            startRow = (Square//3) * 3
            startCol = (Square % 3) * 3

            for i in range(3):
                for j in range(3):
                    row = startRow + i
                    col = startCol + j
                    if board[row][col] == ".":
                        continue
                    if board[row][col] in seenBox:
                        return False
                    seenBox.add(board[row][col])
        return True


            
             


        