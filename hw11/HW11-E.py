# 檔案名稱：HW11-E.py
# 建立日期：2025/12/09
# 檔案說明：感測器數據處理（靜態方法單位轉換＋實體方法狀態記錄）
# 編寫者：monjeychiang


class Sensor:
    def __init__(self):
        # 儲存該感測器的攝氏讀數列表
        self.readings = []

    @staticmethod
    def c_to_f(temp_c):
        # 靜態方法：將攝氏轉換為華氏，不依賴任何實體狀態
        return temp_c * 9 / 5 + 32

    def record(self, temp_c):
        # 實體方法：記錄一筆攝氏溫度
        self.readings.append(temp_c)

    def get_avg_f(self):
        # 實體方法：計算目前所有讀數的平均華氏溫度
        if not self.readings:
            return 0.0
        avg_c = sum(self.readings) / len(self.readings)
        return Sensor.c_to_f(avg_c)


# 建立單一感測器實體
sensor = Sensor()

# 讀取指令數量 N
n = int(input())

# 依序處理 N 筆指令
for _ in range(n):
    parts = input().strip().split()

    # record [temp_c]：記錄一筆攝氏溫度
    if parts[0] == "record":
        temp_c = float(parts[1])
        sensor.record(temp_c)

    # avg_f：輸出目前平均華氏溫度（小數點後 1 位）
    elif parts[0] == "avg_f":
        avg_f = sensor.get_avg_f()
        print(f"{avg_f:.1f}")

    # convert [temp_c]：使用靜態方法做單純的單位轉換
    elif parts[0] == "convert":
        temp_c = float(parts[1])
        temp_f = Sensor.c_to_f(temp_c)
        print(f"{temp_f:.1f}")

