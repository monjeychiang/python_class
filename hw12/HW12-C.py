# 檔案名稱：HW12-C.py
# 建立日期：2025/12/16
# 檔案說明：會員點數共享計畫（@classmethod、類別屬性 vs 實體屬性）
# 編寫者：monjeychiang


class FamilyMember:
    rate = 1.0  # 類別屬性：全家共享的點數倍率

    def __init__(self, name, spend):
        self.name = name
        self.spend = spend  # 實體屬性：個別的消費金額

    @classmethod
    def update_rate(cls, new_rate):
        cls.rate = new_rate

    def calc_points(self):
        return int(self.spend * FamilyMember.rate)


def main():
    command_count = int(input())

    for _ in range(command_count):
        parts = input().split()
        cmd = parts[0]

        if cmd == "member":
            name = parts[1]
            spend = float(parts[2])
            member = FamilyMember(name, spend)
            points = member.calc_points()
            print(f"{name} got {points} points")
        elif cmd == "rate":
            new_rate = float(parts[1])
            FamilyMember.update_rate(new_rate)
            print(f"Rate updated to {FamilyMember.rate}")


if __name__ == "__main__":
    main()
