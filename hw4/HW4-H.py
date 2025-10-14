# 檔案名稱： HW4-H.py
# 建立日期： 2025/10/14
# 檔案說明： 計算考拉茲猜想序列的步驟數和最大值。
# 編輯者： monjeychiang

def collatz_sequence_info(n):
    """
    對於給定的起始數字 n，找出考拉茲序列在變為 1 之前，總共需要多少「步驟」，
    以及在過程中出現的「最大值」是多少。
    """
    if n <= 0:
        return "請輸入一個正整數。"
    
    steps = 0
    max_value = n # 起始數字本身也算是序列的一部分，所以計算最大值時要包含它。
    current_n = n
    
    while current_n != 1:
        if current_n % 2 == 0: # 偶數
            current_n //= 2
        else: # 奇數
            current_n = 3 * current_n + 1
        
        steps += 1
        if current_n > max_value:
            max_value = current_n
            
    return f"Steps: {steps}, Max: {max_value}"

if __name__ == "__main__":
    try:
        N = int(input())
        if N > 0:
            result = collatz_sequence_info(N)
            print(result)
        else:
            print()
    except ValueError:
        print()
