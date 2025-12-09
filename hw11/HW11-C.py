# 檔案名稱：HW11-C.py
# 建立日期：2025/12/09
# 檔案說明：數位錢包匯率系統（類別方法 @classmethod）
# 編寫者：monjeychiang


class Wallet:
    # 類別屬性：所有錢包共用的匯率（從美金換算成當地貨幣）
    rate = 30.0

    def __init__(self, balance):
        # 實體屬性：以美金儲存的餘額
        self.balance = balance

    @classmethod
    def set_rate(cls, new_rate):
        # 類別方法：修改全域匯率設定，影響所有錢包
        cls.rate = new_rate

    def get_local_balance(self):
        # 將美金餘額依目前匯率換算成本地貨幣，並取整數
        return int(self.balance * Wallet.rate)


# 讀取初始美金餘額並建立錢包
initial_balance = float(input())
wallet = Wallet(initial_balance)

# 讀取指令數量 N
n = int(input())

# 依序處理 N 筆指令
for _ in range(n):
    command_line = input().strip().split()

    # set [rate]：修改匯率
    if command_line[0] == "set":
        new_rate = float(command_line[1])
        Wallet.set_rate(new_rate)
    # check：查詢目前當地貨幣金額
    elif command_line[0] == "check":
        print(wallet.get_local_balance())

