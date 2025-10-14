# 檔案名稱： HW4-C.py
# 建立日期： 2025/10/14
# 檔案說明： 根據輸入的 N 和 K，計算 N 的階乘，並找出階乘結果中從右邊數過來第 K 位的數字。
# 編輯者： monjeychiang

def get_kth_digit_from_right(N, K):
    """
    計算 N 的階乘，並找出階乘結果中從右邊數過來第 K 位的數字。
    如果 K 大於階乘結果的總位數，則輸出 0。
    """
    if N < 0:
        return "請輸入非負整數 N。"
    
    # 使用 for 迴圈計算 N 的階乘
    fact_N = 1
    if N == 0:
        fact_N = 1
    else:
        for i in range(1, N + 1):
            fact_N *= i
    
    # 使用 for 迴圈和 %、// 運算提取第 K 位數字
    current_num = fact_N
    for _ in range(K):
        if current_num == 0: # 如果在 K 次迭代前數字變為 0，表示 K 大於總位數
            return 0
        digit = current_num % 10
        current_num //= 10
    
    # 如果迴圈結束後 current_num 仍不為 0，表示找到了第 K 位數字
    # 否則表示 K 大於總位數，應該返回 0
    if current_num == 0 and K > len(str(fact_N)): # 處理 K 恰好等於位數的情況
        return 0
    
    return digit

if __name__ == "__main__":
    try:
        N_str, K_str = input().split()
        N = int(N_str)
        K = int(K_str)

        if 0 <= N <= 20 and 1 <= K <= 25:
            result = get_kth_digit_from_right(N, K)
            print(result)
        else:
            print()
    except ValueError:
        print()
    except IndexError:
        print()
