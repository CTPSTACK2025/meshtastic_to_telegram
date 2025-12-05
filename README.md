[![Traditional Chinese](https://img.shields.io/badge/Language-Traditional%20Chinese-blue)](README.zh-TW.md) [![English](https://img.shields.io/badge/Language-English-blue)](README.md)

# 📡 Meshtastic to Telegram Bridge

A simple, robust Python script that connects to a Meshtastic device via USB (Serial) and forwards all received text messages to a Telegram Chat via a Bot.

## ✨ Features
- **Real-time Forwarding:** Instantly sends received Mesh packets to Telegram.
- **Name Resolution:** Automatically converts Node IDs (e.g., `!12345678`) to friendly User Names (Long/Short names).
- **Auto-Recovery:** Includes logic to detect connection loss and attempt reconnection automatically.
- **Secure:** Uses environment variables for Bot Tokens and Chat IDs.

## 🛠️ Prerequisites

- Python 3.7+
- A Meshtastic Device connected via USB

## 📦 Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/CTPSTACK2025/meshtastic_to_telegram.git
   cd meshtastic_to_telegram
   ```

2. **Install dependencies:**
   ```bash
   pip install meshtastic requests python-dotenv pubsub
   ```

3. **Configuration:**
   Create a `.env` file in the root directory:
   ```ini
   TELEGRAM_BOT_TOKEN=your_bot_token_here
   TELEGRAM_CHAT_ID=your_chat_id_here
   # SERIAL_PORT=/dev/ttyUSB0  <-- Optional: Leave out to auto-detect
   ```

## 🚀 Usage

Run the script:
```bash
python meshtastic_bridge.py
```

## 📝 License
[MIT](LICENSE)
```

