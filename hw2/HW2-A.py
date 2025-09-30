# 檔案名稱：HW2-A.py
# 建立日期：2025/09/30
# 檔案說明：讀取攝氏溫度並轉換為華氏溫度
# 編輯者：monjeychiang

# 提示使用者輸入攝氏溫度
celsius_str = input()

# 將輸入的字串轉換為浮點數
celsius = float(celsius_str)

# 計算華氏溫度
fahrenheit = (celsius * 9/5) + 32

# 使用格式化輸出結果
print(f"{fahrenheit:.1f} ")
