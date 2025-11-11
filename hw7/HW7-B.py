# 檔案名稱： hw7-B.py
# 建立日期： 2025/11/11
# 檔案說明： 讀取3D座標並以元組儲存，然後印出座標資訊卡。
# 編輯者： monjeychiang

# 讀取一行包含三個以空格分隔的整數
x, y, z = map(int, input().split())

# 將座標儲存為元組
coordinates = (x, y, z)

# 印出座標資訊卡
print(f"X: {coordinates[0]}")
print(f"Y: {coordinates[1]}")
print(f"Z: {coordinates[2]}")
