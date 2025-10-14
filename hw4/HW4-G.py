# 檔案名稱： HW4-G.py
# 建立日期： 2025/10/14
# 檔案說明： 計算給定正整數的數字根。
# 編輯者： monjeychiang

def calculate_digital_root(n):
    """
    計算一個正整數的數字根。
    """
    if n < 0:
        return "請輸入一個正整數。"
    
    while n >= 10:
        sum_digits = 0
        # 將數字轉換為字符串，然後遍歷每個數字
        for digit_char in str(n):
            sum_digits += int(digit_char)
        n = sum_digits
    return n

if __name__ == "__main__":
    try:
        N = int(input())
        if N > 0:
            result = calculate_digital_root(N)
            print(result)
        else:
            print()
    except ValueError:
        print()
