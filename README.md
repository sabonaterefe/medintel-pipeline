## MedIntel: ELT Pipeline for Ethiopian Medical Market Intelligence

# Overview
MedIntel is an end-to-end ELT pipeline that extracts, transforms, enriches, and serves content from public Telegram channels in Ethiopia's medical vendor ecosystem. It combines structured modeling (dbt), image enrichment (YOLOv8), orchestration (Dagster), and RESTful serving (FastAPI), all containerized with Docker for reproducibility.

This pipeline is built for monitoring product mentions, visual branding, and channel activity — delivering analytics-ready insights through scheduled jobs and APIs.

# Use Cases
Monitor top-mentioned products across vendor channels

Extract object types (e.g. pills, vials) from shared images

Track channel message frequency and volume trends

Provide RESTful access to search and reporting endpoints

# Architecture Summary
Layer	Tech Used	Purpose
 Ingestion	Telethon	Scrape raw messages from Telegram channels
 Transformation	dbt + PostgreSQL	Clean, validate, and model analytics-ready data
 Enrichment	YOLOv8 via Ultralytics	Detect medical objects in images
 Orchestration	Dagster	Manage pipeline DAGs and execution flow
 Serving	FastAPI	Serve enriched data through REST endpoints
 Deployment	Docker + Compose	Run multi-container stack for reproducible builds
 Project Structure
medintel-pipeline/
├── dags/                     # Dagster orchestration logic
├── dbt/
│   ├── models/
│   │   ├── staging/
│   │   ├── marts/
│   │   │   ├── fct_messages.sql
│   │   │   ├── fct_image_detections.sql ← NEW
│   │   │   ├── dim_channels.sql
│   │   │   └── dim_dates.sql
│   ├── tests/                # dbt validations
│   ├── schema.yml
│   └── dbt_project.yml
├── api/
│   └── main.py               # FastAPI endpoints
├── scripts/
│   └── enrich_images.py      # YOLOv8 enrichment logic
├── docker-compose.yml        # Multi-container stack config
├── Dockerfile                # Python 3.13 base + pipeline tooling
├── pyproject.toml            # Dependency metadata
├── yolov8n.pt                # Pretrained YOLOv8 weights
├── docs/                     # dbt run evidence

# dbt Implementation
Profile name: medintel_pipeline

# Models:

stg_telegram_messages — raw message staging

fct_messages — cleaned message fact table

fct_image_detections — results from YOLO object detection

dim_channels, dim_dates — normalization layers

# Tests:

13 total, including not_null, unique, and custom length checks

# Confirmed:

dbt run, dbt test, dbt docs generate → 

Image Enrichment via YOLOv8
Model: yolov8n.pt loaded from Ultralytics

Script: scripts/enrich_images.py

Pipeline: triggered via Dagster job run_yolo_enrichment

Output Table: fct_image_detections with:

image_id, class_name, confidence, bounding_box

# Example query:

sql
SELECT class_name, COUNT(*) 
FROM marts.fct_image_detections 
GROUP BY class_name 
ORDER BY COUNT DESC;
## Dagster Orchestration
Dagster DAGs run all steps in sequence or on schedule:

# text
Job: scrape_telegram_data
Job: load_raw_to_postgres
Job: run_dbt_transformations
Job: run_yolo_enrichment
To launch Dagster:


docker-compose up dagster
Visit http://localhost:3000 for job graphs, logs, status.

# FastAPI Serving Layer
Accessible endpoints:

/api/search/messages?query=aspirin

/api/channels/lobelia4cosmetics/activity

/api/reports/top-products

# Start FastAPI:

bash
docker-compose up fastapi
Visit http://localhost:8000 or test with tools like Postman.

# Deployment (Docker Compose)
Spin up the entire stack:


docker-compose build
docker-compose up
This initializes:

# Dagster UI on port 3000
# FastAPI on port 8000

# PostgreSQL on port 5432

Environment variables are pulled from .env.

## How to Use
Clone the repo:


git clone https://github.com/sabonaterefe/medintel-pipeline.git
cd medintel-pipeline
Add secrets to .env:

TELEGRAM_API_ID=...
TELEGRAM_API_HASH=...
POSTGRES_USER=...
POSTGRES_PASSWORD=...
Build containers:


docker-compose build
Run the system:


docker-compose up
Access Dagster UI:

http://localhost:3000

Access FastAPI endpoints:

http://localhost:8000

# Limitations
Channel scope: only lobelia4cosmetics and tikvahpharma currently monitored

YOLOv8 uses lightweight n model; consider upgrading to m or l for precision

No pagination or authentication on FastAPI endpoints (yet)

Semantic search (e.g. ChromaDB) planned but not integrated

## Author
Sabona Terefe Machine Learning Engineer specializing in NLP, Pipelines & Search GitHub: @sabonaterefe
