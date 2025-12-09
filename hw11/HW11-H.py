# 檔案名稱：HW11-H.py
# 建立日期：2025/12/09
# 檔案說明：智慧家庭能源管理（家電狀態同步與總耗電量）
# 編寫者：monjeychiang


class Appliance:
    # 類別屬性：整個家庭目前的總耗電量（單位：W）
    total_load = 0

    def __init__(self, name, watts):
        # 實體屬性：家電名稱與耗電瓦數，以及目前是否開啟
        self.name = name
        self.watts = watts
        self.is_on = False

    @staticmethod
    def is_safe_watts(watts):
        # 靜態方法：檢查單一電器瓦數是否安全（不得超過 3000W）
        return watts <= 3000

    def turn_on(self):
        # 實體方法：開啟家電，並將自身瓦數加到總耗電量
        if not self.is_on:
            self.is_on = True
            Appliance.total_load += self.watts

    def turn_off(self):
        # 實體方法：關閉家電，並將自身瓦數從總耗電量扣除
        if self.is_on:
            self.is_on = False
            Appliance.total_load -= self.watts


# 使用字典紀錄已安裝的家電：名稱 -> Appliance 實體
devices = {}

# 讀取指令數量 N
n = int(input())

# 依序處理 N 筆指令
for _ in range(n):
    parts = input().strip().split()
    command = parts[0]

    # add [name] [watts]：安裝家電
    if command == "add":
        name = parts[1]
        watts = int(parts[2])

        # 靜態方法檢查瓦數是否安全
        if not Appliance.is_safe_watts(watts):
            print("Overload Risk")
        else:
            # 安裝（或覆蓋同名家電）
            devices[name] = Appliance(name, watts)
            print("Installed")

    # turn_on [name]：開啟指定家電
    elif command == "turn_on":
        name = parts[1]
        if name in devices:
            devices[name].turn_on()

    # turn_off [name]：關閉指定家電
    elif command == "turn_off":
        name = parts[1]
        if name in devices:
            devices[name].turn_off()

    # status：輸出目前總耗電量
    elif command == "status":
        print(f"Current Load: {Appliance.total_load}W")

