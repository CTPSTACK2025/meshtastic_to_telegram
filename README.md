
```markdown
# 📡 Meshtastic to Telegram Bridge


A robust Python bridge that connects your **Meshtastic LoRa mesh network** to a **Telegram Chat**.

This script listens to a Meshtastic device connected via USB/Serial, resolves the sender's name (User ID -> Friendly Name), and forwards messages to a Telegram Group or Private Chat in real-time.

## ✨ Features

- **🔗 Serial/USB Connection:** Automatically detects and connects to Meshtastic devices (T-Beam, Heltec, RAK, etc.).
- **👤 Name Resolution:** Instead of showing raw Node IDs (e.g., `!289a1c`), it looks up the **friendly username** from the node database.
- **🔄 Auto-Reconnect:** Automatically attempts to reconnect if the device restarts or the USB cable is unplugged.
- **🔒 Secure Configuration:** Uses `.env` files to keep your Telegram tokens safe and out of the code.
- **📝 Logging:** Detailed console logs with timestamps for easier troubleshooting.

## 🛠️ Hardware Requirements

1. A generic computer, Laptop, or **Raspberry Pi** (Recommended for 24/7 operation).
2. A Meshtastic-compatible device (ESP32, nRF52, etc.).
3. A USB data cable.

## 🚀 Installation

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/meshtastic-telegram-bridge.git
cd meshtastic-telegram-bridge
```

### 2. Install Dependencies
You will need Python 3 installed. Install the required libraries:

```bash
pip install meshtastic requests python-dotenv pubsub
```

### 3. Setup Telegram Bot
1. Open Telegram and search for **@BotFather**.
2. Send `/newbot` and follow the instructions to get your **Bot Token**.
3. Create a group (or use a private chat) and add your bot to it.
4. Get your **Chat ID** (You can forward a message to `@userinfobot` or use the API to find it).

### 4. Configuration (.env)
Create a file named `.env` in the project folder:

```bash
nano .env
```

Paste your credentials inside:

```ini
TELEGRAM_BOT_TOKEN=123456789:ABCdefGHIjklMNOpqrsTUVwxyz
TELEGRAM_CHAT_ID=-1001234567890
```
*Note: If sending to a group topic, the Chat ID usually starts with `-100`.*

## 🏃 Usage

Run the script:

```bash
python main.py
```

**Expected Output:**
```text
2023-10-27 10:00:01 - INFO - Starting Meshtastic to Telegram Bridge...
2023-10-27 10:00:03 - INFO - ✅ Connected to radio on /dev/ttyUSB0
```

## ⚙️ Running as a Service (Linux/Raspberry Pi)

To keep the bridge running 24/7 in the background and restart automatically on boot:

1. Create a service file:
   ```bash
   sudo nano /etc/systemd/system/meshbridge.service
   ```

2. Paste the following (adjust paths to match your setup):
   ```ini
   [Unit]
   Description=Meshtastic Telegram Bridge
   After=network.target

   [Service]
   User=pi
   WorkingDirectory=/home/pi/meshtastic-telegram-bridge
   ExecStart=/usr/bin/python3 /home/pi/meshtastic-telegram-bridge/main.py
   Restart=always
   RestartSec=10

   [Install]
   WantedBy=multi-user.target
   ```

3. Enable and start the service:
   ```bash
   sudo systemctl enable meshbridge
   sudo systemctl start meshbridge
   ```

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

## 📄 License

[MIT](https://choosealicense.com/licenses/mit/)
```
