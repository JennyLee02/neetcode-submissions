class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        # validate rows
        for i in range(9):
            row = set()
            for j in range(9):
                item = board[i][j]
                if item in row:
                    return False
                elif item != '.':
                    row.add(item)
        
        # validate col
        for i in range(9):
            row = set()
            for j in range(9):
                item = board[j][i]
                if item in row:
                    return False
                elif item != '.':
                    row.add(item)
        
        # validate 3*3 boxes
        boxes = defaultdict(set)
        for i in range(9):
            for j in range(9):
                item = board[i][j]
                box = (i//3, j//3)
                if item in boxes[box]:
                    return False
                elif item != '.':
                    boxes[box].add(item)

        return True
                