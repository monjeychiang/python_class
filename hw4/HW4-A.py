# 檔案名稱： HW4-A.py
# 建立日期： 2025/10/14
# 檔案說明： 根據輸入的正整數 N，印出一個高度為 N 層的數字金字塔。
# 編輯者： monjeychiang

def print_number_pyramid(N):
    """
    根據輸入的正整數 N，印出一個高度為 N 層、每層數字從 1 到 i 的數字金字塔。
    """
    for i in range(1, N + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()

if __name__ == "__main__":
    try:
        N = int(input())
        if N > 0:
            print_number_pyramid(N)
        else:
            print()
    except ValueError:
        print()
