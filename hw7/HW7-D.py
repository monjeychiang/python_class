# 檔案名稱： hw7-d.py
# 建立日期： 2025/11/11
# 檔案說明： 設計一個候位系統來模擬餐廳的顧客隊伍。
# 編輯者： monjeychiang

# 初始化候位隊伍
waiting_line = []

# 持續讀取指令直到 EXIT
while True:
    command_line = input()
    
    # EXIT 指令
    if command_line == "EXIT":
        break
        
    # 分割指令以處理 WAIT
    parts = command_line.split()
    command = parts[0]
    
    # WAIT 指令
    if command == "WAIT":
        name = parts[1]
        waiting_line.append(name)
    # CALL 指令
    elif command == "CALL":
        if waiting_line:
            # 隊伍有人，呼叫第一位
            name = waiting_line.pop(0)
            print(f"Call: {name}")
        else:
            # 隊伍是空的
            print("No one in line")
