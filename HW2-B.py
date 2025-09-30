# 檔案名稱：HW2-B.py
# 建立日期：2025/09/30
# 檔案說明：讀取圓的半徑並計算面積
# 編輯者：monjeychiang

import math

# 提示使用者輸入半徑
radius_str = input()

# 將輸入的字串轉換為浮點數
radius = float(radius_str)

# 計算圓面積
area = math.pi * (radius ** 2)

# 使用格式化輸出結果
print(f"{area:.2f}")
