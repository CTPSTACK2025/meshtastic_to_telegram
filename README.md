# meshtastic_to_telegram
# Meshtastic to Telegram Bridge 📡 -> 📱

A simple Python script that listens to a Meshtastic device via USB (Serial) and forwards all received text messages to a Telegram Chat or Group.

## Features
- **Auto-Connect:** Automatically detects the Meshtastic device on the first available Serial/USB port.
- **Real-time Forwarding:** Instantly sends received LoRa messages to Telegram via Bot API.
- **Sender Identification:** Includes the sender's ID in the Telegram notification.

## Prerequisites
- A Meshtastic Device connected via USB.
- Python 3.x installed.
- A Telegram Bot Token and Chat ID.

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/CTPSTACK2025/meshtastic_to_telegram.git
   cd meshtastic-telegram-bridge
