# 檔案名稱： HW4-B.py
# 建立日期： 2025/10/14
# 檔案說明： 根據輸入的正整數 N，計算交錯數列 S = 1 - 2 + 3 - 4 + ... ± N 的總和。
# 編輯者： monjeychiang

def calculate_alternating_sum(N):
    """
    計算交錯數列 S = 1 - 2 + 3 - 4 + ... ± N 的總和。
    奇數項為正，偶數項為負。
    """
    total_sum = 0
    for i in range(1, N + 1):
        if i % 2 == 1:  # 奇數項
            total_sum += i
        else:  # 偶數項
            total_sum -= i
    return total_sum

if __name__ == "__main__":
    try:
        N = int(input())
        if N > 0:
            result = calculate_alternating_sum(N)
            print(result)
        else:
            print()
    except ValueError:
        print()
