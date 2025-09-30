# 檔案名稱：HW2-C.py
# 建立日期：2025/09/30
# 檔案說明：讀取矩形的長和寬並計算對角線長度
# 編輯者：monjeychiang

import math

# 提示使用者輸入長度和寬度，以空格分隔
input_str = input()

# 將輸入的字串以空格分割，並轉換為浮點數
length_str, width_str = input_str.split()
length = float(length_str)
width = float(width_str)

# 計算對角線長度
diagonal = math.sqrt(length**2 + width**2)

# 使用格式化輸出結果
print(f"{diagonal:.2f}")
