# 檔案名稱：HW2-E.py
# 建立日期：2025/09/30
# 檔案說明：讀取一個分數並判斷其級距
# 編輯者：monjeychiang

# 提示使用者輸入分數
score_str = input()

# 將輸入的字串轉換為浮點數
score = float(score_str)

# 初始化級距變數
grade = ""

# 判斷分數級距
if score >= 90:
    grade = "A"
elif score >= 75:
    grade = "B"
elif score >= 50 and score < 70:
    grade = "C"
elif score < 50:
    grade = "F"
else:
    grade = "no"

# 輸出結果
print(f"{grade}")
