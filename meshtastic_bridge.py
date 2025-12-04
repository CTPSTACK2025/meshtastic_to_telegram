import time
import os
import sys
import logging
import requests
import meshtastic
import meshtastic.serial_interface
from pubsub import pub
from dotenv import load_dotenv

# --- Setup Logging ---
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
logger = logging.getLogger(__name__)

# --- Load Configuration ---
load_dotenv() # Loads variables from .env file
TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
CHAT_ID = os.getenv('TELEGRAM_CHAT_ID')
SERIAL_PORT = None # Set to None for auto-detect

if not TOKEN or not CHAT_ID:
    logger.error("❌ Missing .env configuration. Please check TELEGRAM_BOT_TOKEN and TELEGRAM_CHAT_ID.")
    sys.exit(1)

# Global interface reference for node lookups
mesh_interface = None

def get_node_name(node_id):
    """Resolves a Node ID to a Long Name or Short Name."""
    if mesh_interface and mesh_interface.nodes:
        node = mesh_interface.nodes.get(node_id)
        if node:
            user = node.get('user', {})
            return user.get('longName') or user.get('shortName') or user.get('id')
    return node_id  # Fallback to ID if name not found

def send_telegram_message(message):
    """Sends a message to the configured Telegram chat."""
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    data = {
        "chat_id": CHAT_ID,
        "text": message,
        "parse_mode": "HTML"
    }
    
    try:
        # Added timeout to prevent hanging
        response = requests.post(url, data=data, timeout=10)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        logger.error(f"❌ Failed to send to Telegram: {e}")

def on_receive(packet, interface):
    """Callback function triggered when a packet is received."""
    try:
        if 'decoded' in packet and 'text' in packet['decoded']:
            msg_text = packet['decoded']['text']
            sender_id = packet.get('fromId')
            
            # Resolve the nice name
            sender_name = get_node_name(sender_id)
            
            # Log to console
            logger.info(f"📩 Message from {sender_name}: {msg_text}")
            
            # Send to Telegram
            formatted_msg = (
                f"📡 <b>Meshtastic Bridge</b>\n"
                f"👤 <b>From:</b> {sender_name}\n"
                f"💬 <b>Message:</b>\n{msg_text}"
            )
            send_telegram_message(formatted_msg)
            
    except Exception as e:
        logger.error(f"Error parsing packet: {e}")

def main():
    global mesh_interface
    
    logger.info("Starting Meshtastic to Telegram Bridge...")
    
    while True:
        try:
            # Initialize the interface
            mesh_interface = meshtastic.serial_interface.SerialInterface(devPath=SERIAL_PORT)
            
            # Subscribe to message events
            pub.subscribe(on_receive, "meshtastic.receive")
            
            logger.info(f"✅ Connected to radio on {mesh_interface.devPath}")
            send_telegram_message("🚀 <b>System:</b> Bridge connected successfully.")
            
            # Keep the script running and monitor connection
            while True:
                time.sleep(1)
                # Optional: Check if interface is still alive
                if not mesh_interface.nodes:
                    raise Exception("Interface appears disconnected")

        except PermissionError:
            logger.error("❌ Permission denied accessing serial port. Try using 'sudo'.")
            sys.exit(1)
        except OSError as e:
            logger.warning(f"⚠️ Connection lost or device not found: {e}. Retrying in 5 seconds...")
            if mesh_interface:
                mesh_interface.close()
            time.sleep(5)
        except KeyboardInterrupt:
            logger.info("🛑 Stopping Bridge...")
            if mesh_interface:
                mesh_interface.close()
            sys.exit(0)
        except Exception as e:
            logger.error(f"❌ Unexpected error: {e}. Restarting loop...")
            time.sleep(5)

if __name__ == "__main__":
    main()