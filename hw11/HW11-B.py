# 檔案名稱：HW11-B.py
# 建立日期：2025/12/09
# 檔案說明：密碼強度驗證器（靜態方法 @staticmethod）
# 編寫者：monjeychiang


class Security:
    # 靜態方法：只做邏輯判斷，不需要使用物件或類別屬性
    @staticmethod
    def is_valid(password):
        """
        若密碼長度 >= 6 且包含至少一個數字，回傳 True，否則 False。
        """
        # 長度需至少 6
        if len(password) < 6:
            return False

        # 至少包含一個數字
        has_digit = any(ch.isdigit() for ch in password)

        return has_digit


# 讀取要檢查的密碼數量 N
n = int(input())

# 依序讀取 N 個測試密碼並檢查強度
for _ in range(n):
    pwd = input().strip()
    if Security.is_valid(pwd):
        print("Valid")
    else:
        print("Weak")

