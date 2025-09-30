# 檔案名稱：HW2-D.py
# 建立日期：2025/09/30
# 檔案說明：讀取一個整數並判斷其為奇數或偶數
# 編輯者：monjeychiang

# 提示使用者輸入一個整數
num_str = input()

# 將輸入的字串轉換為整數
num = int(num_str)

# 使用算術運算子判斷奇偶數
if num % 2 == 0:
    result = "Even"
else:
    result = "Odd"

# 輸出結果
print(f"{result}")
