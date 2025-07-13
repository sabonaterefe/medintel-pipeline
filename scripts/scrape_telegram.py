import os
import json
import logging
from datetime import datetime
from telethon import TelegramClient
from telethon.tl.types import MessageMediaPhoto
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
API_ID = int(os.getenv("TELEGRAM_API_ID"))
API_HASH = os.getenv("TELEGRAM_API_HASH")
SESSION_NAME = os.getenv("SESSION_NAME") or "medintel-pipeline"

# Define channels to scrape
CHANNELS = {
    "lobelia4cosmetics": "https://t.me/lobelia4cosmetics",
    "tikvahpharma": "https://t.me/tikvahpharma",
}

# File paths
DATA_DIR = "data/raw/telegram_messages"
IMAGE_DIR = "data/yolo_outputs"
LOG_FILE = "data/scrape_log.txt"

# Setup logging
logging.basicConfig(filename=LOG_FILE, level=logging.INFO)

# Create Telegram client instance
client = TelegramClient(SESSION_NAME, API_ID, API_HASH)

async def scrape_channel(channel_name, channel_url):
    try:
        await client.start()  # Prompts for phone number once on first run
        entity = await client.get_entity(channel_url)
        messages = []

        async for message in client.iter_messages(entity, limit=200):
            msg_info = {
                "id": message.id,
                "text": message.message,
                "date": str(message.date),
                "channel": channel_name,
                "has_image": isinstance(message.media, MessageMediaPhoto)
            }

            if msg_info["has_image"]:
                image_path = os.path.join(IMAGE_DIR, f"{channel_name}_{message.id}.jpg")
                await client.download_media(message.media, file=image_path)
                msg_info["image_path"] = image_path

            messages.append(msg_info)

        # Save messages to JSON
        date_folder = datetime.now().strftime("%Y-%m-%d")
        os.makedirs(os.path.join(DATA_DIR, date_folder), exist_ok=True)
        out_file = os.path.join(DATA_DIR, date_folder, f"{channel_name}.json")

        with open(out_file, "w", encoding="utf-8") as f:
            json.dump(messages, f, indent=2, ensure_ascii=False)

        logging.info(f"Scraped {len(messages)} messages from {channel_name}")

    except Exception as e:
        logging.error(f"Error scraping {channel_name}: {e}")

async def main():
    for name, url in CHANNELS.items():
        await scrape_channel(name, url)

if __name__ == "__main__":
    with client:
        client.loop.run_until_complete(main())
