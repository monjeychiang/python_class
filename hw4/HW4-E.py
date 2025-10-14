# 檔案名稱： HW4-E.py
# 建立日期： 2025/10/14
# 檔案說明： 根據輸入的兩個正整數 A 和 B，找出它們的最大公因數 (GCD) 和最小公倍數 (LCM)。
# 編輯者： monjeychiang

def calculate_gcd(a, b):
    """
    使用 for 迴圈計算兩個數字的最大公因數 (GCD)。
    """
    min_val = min(a, b)
    gcd = 1
    for i in range(1, min_val + 1):
        if a % i == 0 and b % i == 0:
            gcd = i
    return gcd

def calculate_lcm(a, b):
    """
    計算兩個數字的最小公倍數 (LCM)。
    """
    if a == 0 or b == 0:
        return 0
    # 直接使用公式計算 LCM，避免額外的迴圈
    return (a * b) // calculate_gcd(a, b)

if __name__ == "__main__":
    try:
        A_str, B_str = input().split()
        A = int(A_str)
        B = int(B_str)

        if A <= 0 or B <= 0:
            print()
        else:
            gcd_result = calculate_gcd(A, B)
            lcm_result = calculate_lcm(A, B)
            print(f"GCD: {gcd_result}, LCM: {lcm_result}")
    except ValueError:
        print()
    except IndexError:
        print()
