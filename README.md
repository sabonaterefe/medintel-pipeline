# A Modern ELT Platform for Ethiopian Medical Market Intelligence
##  Overview

MedIntel is an ELT pipeline that extracts public Telegram data from Ethiopian medical vendors and transforms it into a structured, queryable data warehouse. It supports analytics around posting trends, visual content, and product mentions.

---

## Key Business Questions

- What are the top-mentioned medical products or drugs?
- How does product availability vary across channels?
- Which channels feature the most visual content?
- What are the daily/weekly trends in posting volume?

---

##  Architecture

Telegram → JSON → PostgreSQL → dbt → YOLOv8 → FastAPI


| Layer         | Tools Used                    |
|---------------|-------------------------------|
| Extraction     | Telethon                     |
| Loading        | Python + psycopg2            |
| Transformation | dbt + PostgreSQL             |
| Enrichment     | YOLOv8 *(task 3)*            |
| Serving        | FastAPI *(task 4)*           |
| Orchestration  | Dagster *(task 5)*           |

---

## Project Structure

medintel-pipeline/
├── api/                  # FastAPI server
├── dags/                 # Dagster orchestrations
├── dbt/medintel_models/  # dbt transformations
├── docker/               # Docker configs
├── scripts/              # Scraper & loader
├── data/
│   └── raw/              # Raw Telegram messages
│   └── yolo_outputs/     # Saved images
├── requirements.txt
├── dbt_project.yml
└── .env (excluded from Git)
Installation
git clone https://github.com/sabonaterefe/medintel-pipeline.git
cd medintel-pipeline
docker-compose up -d
Create a .env file using python-dotenv to hold your credentials.

Usage
Run loader:

python scripts/load_to_postgres.py
Run transformations:

dbt run --full-refresh
dbt test
Query results:

sql
SELECT * FROM staging.fct_messages LIMIT 5;
dbt Model Lineage
raw.telegram_messages → stg_telegram_messages

stg_telegram_messages + dim_channels, dim_dates → fct_messages

Each model has a documented schema with descriptions and constraints.

Metrics Available
message_length

has_image

image_path

message_date

Foreign keys to dim_channels and dim_dates

Tests & Validation
Primary key tests (unique, not_null)

Custom test: prevent message_length <= 1

All models pass dbt test 

Sample Output
SELECT channel, COUNT(*) AS message_count
FROM staging.fct_messages
GROUP BY channel
ORDER BY message_count DESC;

Limitations
Currently supports two channels (lobelia4cosmetics, tikvahpharma)

Image detection not yet applied (YOLOv8 prep complete)

Future Work
YOLO enrichment of images

Serving insights via FastAPI

Orchestration with Dagster

Semantic retrieval using ChromaDB

Author
Sabona Terefe ML Engineer | NLP | Semantic Search GitHub: @sabonaterefe
