# 檔案名稱：HW2-F.py
# 建立日期：2025/09/30
# 檔案說明：讀取一個西元年份並判斷其是否為閏年
# 編輯者：monjeychiang

# 提示使用者輸入西元年份
year_str = input()

# 將輸入的字串轉換為整數
year = int(year_str)

# 判斷是否為閏年
# 規則：
# 1. 可被 4 整除，但不能被 100 整除，為閏年。
# 2. 可被 400 整除，為閏年。
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    result = "Leap Year"
else:
    result = "Not a Leap Year"

# 輸出結果
print(f"{result}")
