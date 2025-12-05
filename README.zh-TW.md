***

# 📡 Meshtastic 至 Telegram 轉發器

這是一個簡單且穩定的 Python 程式，能夠透過 USB (Serial 序列埠) 連接 Meshtastic 裝置，並利用 Bot 將所有接收到的文字訊息轉發至 Telegram 聊天室。

## ✨ 功能特色
- **即時轉發 (Real-time Forwarding)：** 瞬間將接收到的 Mesh 封包傳送至 Telegram。
- **名稱解析 (Name Resolution)：** 自動將節點 ID (例如 `!12345678`) 轉換為易讀的用戶名稱 (長名/短名)。
- **自動重連 (Auto-Recovery)：** 內建連線中斷偵測邏輯，並會嘗試自動重新連接。
- **安全性 (Secure)：** 使用環境變數來管理 Bot Token 和 Chat ID。

## 🛠️ 系統需求

- Python 3.7 或以上版本
- 一台透過 USB 連接的 Meshtastic 裝置

## 📦 安裝教學

1. **複製 (Clone) 專案儲存庫：**
   ```bash
   git clone https://github.com/CTPSTACK2025/meshtastic_to_telegram.git
   cd meshtastic_to_telegram
   ```

2. **安裝相依套件：**
   ```bash
   pip install meshtastic requests python-dotenv pubsub
   ```

3. **設定檔配置：**
   在專案根目錄下建立一個 `.env` 檔案：
   ```ini
   TELEGRAM_BOT_TOKEN=你的_bot_token
   TELEGRAM_CHAT_ID=你的_chat_id
   # SERIAL_PORT=/dev/ttyUSB0  <-- 可選：若不設定則會嘗試自動偵測
   ```

## 🚀 使用方法

執行程式：
```bash
python meshtastic_bridge.py
```

## 📝 授權條款
[MIT](LICENSE)
