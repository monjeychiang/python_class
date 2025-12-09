# 檔案名稱：HW11-G.py
# 建立日期：2025/12/09
# 檔案說明：遊戲伺服器全服活動（全服倍率控制）
# 編寫者：monjeychiang


class GameServer:
    # 類別屬性：全服經驗值倍率（預設 1.0）
    rate = 1.0

    @classmethod
    def set_rate(cls, new_rate):
        # 類別方法：設定全服經驗倍率
        cls.rate = new_rate

    @staticmethod
    def is_valid_name(name):
        # 靜態方法：檢查玩家名稱是否包含髒話 "bad"
        return "bad" not in name


class Player:
    def __init__(self, name):
        # 實體屬性：玩家名稱
        self.name = name

    def get_exp(self, monster_xp):
        # 實體方法：計算打怪後實際獲得的經驗值
        return int(monster_xp * GameServer.rate)


# 讀取指令數量 N
n = int(input())

# 依序處理 N 筆指令
for _ in range(n):
    parts = input().strip().split()

    # event [rate]：設定全服倍率
    if parts[0] == "event":
        rate = float(parts[1])
        GameServer.set_rate(rate)
        print("Global Rate Updated")

    # player [name] [monster_xp]：建立玩家並模擬打怪
    elif parts[0] == "player":
        name = parts[1]
        monster_xp = int(parts[2])

        # 先檢查名稱是否含有 "bad"
        if not GameServer.is_valid_name(name):
            print("Banned Name")
        else:
            player = Player(name)
            gained = player.get_exp(monster_xp)
            print(f"{player.name} gained {gained} XP")
