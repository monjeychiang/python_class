# 檔案名稱： HW7-G.py
# 建立日期： 2025/11/11
# 檔案說明： 判斷井字遊戲 (Tic-Tac-Toe) 中 X 是否獲勝。
# 編輯者： monjeychiang

# 讀取 3x3 棋盤狀態
board = []
for _ in range(3):
    board.append(list(input().strip())) # 移除行尾的空白字元，例如 \r

# 檢查 X 是否獲勝的函數
def check_win(board):
    # 檢查行
    for row in board:
        if all(cell == 'X' for cell in row):
            return True
    
    # 檢查列
    for col in range(3):
        if all(board[row][col] == 'X' for row in range(3)):
            return True
            
    # 檢查主對角線 (左上到右下)
    if all(board[i][i] == 'X' for i in range(3)):
        return True
        
    # 檢查副對角線 (右上到左下)
    if all(board[i][2-i] == 'X' for i in range(3)):
        return True
        
    return False

# 判斷並印出結果
if check_win(board):
    print("X wins")
else:
    print("In progress or Draw")
