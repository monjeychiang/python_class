# 檔案名稱： HW7-H.py
# 建立日期： 2025/11/11
# 檔案說明： 實作即時計算數據串流中位數的功能。
# 編輯者： monjeychiang

# 讀取數字總數 N
n = int(input())

# 儲存數據的串列
data_stream = []

# 讀取 N 個數字並計算中位數
for _ in range(n):
    num = int(input())
    data_stream.append(num)
    data_stream.sort() # 每次加入新數字後排序

    current_len = len(data_stream)
    
    if current_len % 2 == 1:
        # 奇數個數字，中位數是中間的數字
        median = float(data_stream[current_len // 2])
    else:
        # 偶數個數字，中位數是中間兩個數字的平均值
        mid1 = data_stream[current_len // 2 - 1]
        mid2 = data_stream[current_len // 2]
        median = (float(mid1) + float(mid2)) / 2.0
        
    # 印出中位數，格式化為浮點數
    print(f"{median:.1f}")
