import os
import json
import psycopg2
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# PostgreSQL connection
DB_CONN = psycopg2.connect(
    dbname=os.getenv("POSTGRES_DB"),
    user=os.getenv("POSTGRES_USER"),
    password=os.getenv("POSTGRES_PASSWORD"),
    host=os.getenv("POSTGRES_HOST"),
    port=os.getenv("POSTGRES_PORT"),
)

DATA_DIR = "data/raw/telegram_messages"

def load_json(folder):
    total_inserted = 0
    for date_folder in os.listdir(folder):
        date_path = os.path.join(folder, date_folder)
        if not os.path.isdir(date_path):
            continue

        for filename in os.listdir(date_path):
            if not filename.endswith(".json"):
                continue

            file_path = os.path.join(date_path, filename)
            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    messages = json.load(f)
                    inserted = insert_into_db(messages)
                    total_inserted += inserted
                    print(f"✓ Loaded {inserted} messages from {filename}")
            except Exception as e:
                print(f"⚠️ Failed to load {filename}: {e}")

    print(f"\n✅ Finished loading. Total messages inserted: {total_inserted}")

def insert_into_db(messages):
    cursor = DB_CONN.cursor()
    inserted_count = 0

    for msg in messages:
        try:
            cursor.execute("""
                INSERT INTO raw.telegram_messages (id, text, date, channel, has_image, image_path)
                VALUES (%s, %s, %s, %s, %s, %s)
                ON CONFLICT (id) DO NOTHING;
            """, (
                msg["id"],
                msg["text"],
                msg["date"],
                msg["channel"],
                msg["has_image"],
                msg.get("image_path")
            ))
            inserted_count += 1
        except Exception as e:
            print(f"⚠️ Error inserting message ID {msg.get('id')}: {e}")

    DB_CONN.commit()
    cursor.close()
    return inserted_count

if __name__ == "__main__":
    try:
        load_json(DATA_DIR)
    finally:
        DB_CONN.close()
        print("🧵 Database connection closed.")
