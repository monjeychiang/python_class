# 檔案名稱：HW12-D.py
# 建立日期：2025/12/16
# 檔案說明：倉儲進出貨管理（Set 操作、實體方法、物件狀態）
# 編寫者：monjeychiang


class Warehouse:
    def __init__(self, items):
        self.inventory = set(items)  # 目前有貨的商品
        self.missing = []  # 缺貨清單

    def order(self, item):
        if item in self.inventory:
            print("Shipped")
        else:
            self.missing.append(item)
            print("Out of Stock")

    def restock(self, item):
        self.inventory.add(item)


def main():
    initial_items = input().split()
    warehouse = Warehouse(initial_items)

    command_count = int(input())
    for _ in range(command_count):
        parts = input().split()
        cmd, item = parts[0], parts[1]

        if cmd == "order":
            warehouse.order(item)
        elif cmd == "restock":
            warehouse.restock(item)

    print(f"Total Missing: {len(warehouse.missing)}")


if __name__ == "__main__":
    main()
