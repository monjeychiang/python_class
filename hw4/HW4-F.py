# 檔案名稱： HW4-F.py
# 建立日期： 2025/10/14
# 檔案說明： 模擬一個猜數字遊戲，程式預設祕密數字為 77，玩家需猜中數字。
# 編輯者： monjeychiang

def guess_the_number_game():
    """
    模擬猜數字遊戲，直到玩家猜中祕密數字 77 為止。
    """
    SECRET_NUMBER = 77
    
    while True:
        try:
            guess = int(input())
            
            if guess > SECRET_NUMBER:
                print("Too high")
            elif guess < SECRET_NUMBER:
                print("Too low")
            else:
                print("Correct!")
                break # 猜中後結束遊戲
        except ValueError:
            # 根據題目要求，只處理整數輸入，非整數輸入不給予提示，但會導致程式崩潰
            # 為了讓程式能持續運行，這裡可以選擇忽略或給予錯誤提示
            # 根據題目描述，程式會持續讀取玩家輸入的整數，所以這裡不處理非整數輸入的錯誤，讓其崩潰
            # 如果需要更健壯的處理，可以加上 print("無效的輸入。請輸入一個整數。")
            pass

if __name__ == "__main__":
    guess_the_number_game()
