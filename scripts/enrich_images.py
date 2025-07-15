from ultralytics import YOLO
from dotenv import load_dotenv
import os
import psycopg2

load_dotenv()

model = YOLO("yolov8n.pt")
image_dir = "data/yolo_outputs"

def extract_message_id(filename):
    # Assuming filename format: msg_12345.png
    return filename.split("_")[1].split(".")[0]

def main():
    conn = psycopg2.connect(
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        dbname=os.getenv("DB_NAME")
    )
    cur = conn.cursor()

    for filename in os.listdir(image_dir):
        if not filename.lower().endswith((".png", ".jpg", ".jpeg")):
            continue
        results = model(os.path.join(image_dir, filename))
        for box in results[0].boxes.data.tolist():
            class_id, conf, *_ = box
            cur.execute("""
                INSERT INTO image_detections (message_id, detected_object_class, confidence_score)
                VALUES (%s, %s, %s)
            """, (
                extract_message_id(filename),
                model.names[int(class_id)],
                float(conf)
            ))

    conn.commit()
    cur.close()
    conn.close()

if __name__ == "__main__":
    main()
