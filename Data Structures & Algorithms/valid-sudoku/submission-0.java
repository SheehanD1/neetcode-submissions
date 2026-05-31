class Solution {
    public boolean isValidSudoku(char[][] board) {
        for (int i = 0; i < 9; i++) {
            Set<Character> rowSet = new HashSet<>();
            Set<Character> colSet = new HashSet<>();
            Set<Character> boxSet = new HashSet<>();
            for (int j = 0; j < 9; j++) {
                char rowVal = board[i][j];
                if (rowVal != '.') {
                    if (!rowSet.add(rowVal)) return false;
                }
                char colVal = board[j][i];
                if (colVal != '.') {
                    if (!colSet.add(colVal)) return false;
                }
                int rowIndex = 3 * (i / 3);
                int colIndex = 3 * (i % 3);
                char boxVal = board[rowIndex + j / 3][colIndex + j % 3];
                if (boxVal != '.') {
                    if (!boxSet.add(boxVal)) return false;
                }
            }
        }
        return true;
    }
}
