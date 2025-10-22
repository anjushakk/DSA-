class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # If only one row or shorter string, no zigzag needed
        if numRows == 1 or numRows >= len(s):
            return s

        # Create an array of strings for each row
        rows = [''] * numRows
        cur_row = 0
        going_down = False

        for ch in s:
            rows[cur_row] += ch
            # Change direction if top or bottom is reached
            if cur_row == 0 or cur_row == numRows - 1:
                going_down = not going_down
            # Move up or down
            cur_row += 1 if going_down else -1

        # Combine all rows
        return ''.join(rows)
