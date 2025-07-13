## MedIntel is a modular ELT platform designed to transform public Telegram content from Ethiopian medical vendors into an analytics-ready warehouse. It supports trend monitoring, product tracking, and content enrichment using dbt, YOLOv8, and FastAPI.

# Business Questions

Which products or medications are most frequently mentioned?

How does product visibility differ by Telegram channel?

What channels contain the most visual content?

What are the daily and weekly posting trends?

Architecture & Flow Telegram → JSON → PostgreSQL → dbt → YOLOv8 → FastAPI → Dagster

Tools by layer: Extraction: Telethon Loading: Python with psycopg2 Transformation: dbt and PostgreSQL Enrichment: YOLOv8 (Task 3) Serving: FastAPI (Task 4) Orchestration: Dagster (Task 5)

# Project Structure The pipeline is organized into the following directories:

api: FastAPI server code

dags: Dagster orchestration definitions

dbt/medintel_models: dbt models, sources, and tests

staging: includes schema.yml and stg_telegram_messages.sql

marts: includes fct_messages.sql, dim_channels.sql, dim_dates.sql

tests: includes custom test long_messages.sql

scripts: Telegram scraping and loading utilities

# data:

raw: contains original scraped Telegram messages

yolo_outputs: stores object detection results

requirements.txt: Python dependencies

dbt_project.yml: dbt configuration

.env: stores environment variables (excluded from version control)

# Installation Clone the repository and start the pipeline:

git clone https://github.com/sabonaterefe/medintel-pipeline.git

cd medintel-pipeline

docker-compose up -d Create an .env file with your credentials using python-dotenv.

# Usage To load data:
Run python scripts/load_to_postgres.py

To transform and test: Run dbt run and dbt test

To generate and view documentation: Run dbt docs generate followed by dbt docs serve Then open http://localhost:8080 in your browser

Query example: SELECT * FROM staging.fct_messages LIMIT 5;

Model Lineage raw.telegram_messages → stg_telegram_messages stg_telegram_messages + dim_channels and dim_dates → fct_messages

# All models include documented schemas with descriptions and constraints.

Model Summaries stg_telegram_messages: filters and normalizes raw Telegram messages dim_channels: maps known Telegram channels dim_dates: provides a time dimension fct_messages: fact table combining message content and metadata

Metrics Available

message_length

has_image

image_path

message_date

channel associations via foreign keys

# Tests and Validation

not_null and unique checks on primary keys

Custom test to reject messages with message_length <= 1

All tests passing with dbt test

Sample Query SELECT channel, COUNT(*) AS message_count FROM staging.fct_messages GROUP BY channel ORDER BY message_count DESC;

# Limitations

Currently supports two channels: lobelia4cosmetics and tikvahpharma

YOLOv8 enrichment is prepared but not executed

Semantic retrieval with ChromaDB is not yet integrated

# Future Enhancements

YOLOv8 enrichment of image content

FastAPI endpoint for querying insights

Pipeline orchestration via Dagster

Semantic search and clustering with ChromaDB and embeddings

## Author Sabona Terefe Machine Learning Engineer specializing in NLP and Semantic Search GitHub: @sabonaterefe
