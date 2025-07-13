# A Modern ELT Platform for Ethiopian Medical Market Intelligence
Project Overview:
Kara Solutions aims to empower analytical decision-making in Ethiopia’s health sector. This pipeline extracts public Telegram data from local medical vendors and transforms it into structured, enriched, and queryable insights.

Key questions for this work are like:

What drugs or products are most discussed across channels?

How does content vary by vendor (visual vs. textual)?

Which days show spikes in medical-related posting activity?

How do image patterns differ between pill-based and cosmetic ads?

Architecture Summary: 

Telegram ➜ Raw JSON ➜ PostgreSQL ➜ dbt Star Schema ➜ Enrichment + Analytics
Layer	Tool/Tech	Purpose
Extraction	Telethon (Python)	Scrape message text + images from channels
Storage	File System (JSON)	Partitioned raw lake per date & channel
Ingestion	psycopg2 (Python)	Load into raw.telegram_messages table
Transformation	dbt	Create staging + star schema models
Enrichment	YOLOv8	(Task 3) Detect objects in saved images
Serving	FastAPI	(Task 4) Expose enriched insights via API
Orchestration	Dagster	(Task 5) Automate ELT with asset scheduling

Algorithms & Technical Approach
Extraction:

Telethon API for Telegram scraping:

Configured with session name and credentials

Extracts text, date, channel, and media presence

Structured file naming: data/raw/telegram_messages/YYYY-MM-DD/channel_name.json

Image assets: Stored as data/yolo_outputs/channel_msgid.jpg

Loading:

Python Loader Script (load_to_postgres.py):

Reads JSON, parses records

Inserts into PostgreSQL via psycopg2

Uses ON CONFLICT DO NOTHING to gracefully skip duplicates

Transformation:

dbt for SQL-based ELT modeling

Models built:

stg_telegram_messages.sql (cleansing, casting)

dim_channels.sql (channel metadata)

dim_dates.sql (posting timeline)

fct_messages.sql (message metrics incl. image path & length)

Star schema design

dbt tests:

unique, not_null on keys

Custom data integrity rule

Project Structure
bash
medintel-pipeline/
├── api/                        # FastAPI endpoint (Task 4)
├── dags/                       # Dagster pipeline (Task 5)
├── dbt/medintel_models/        # dbt transformations & tests
├── docker/                     # Docker config & services
├── scripts/                    # Scraping & ingestion logic
├── data/
│   └── raw/                    # Channel-level Telegram dumps
│   └── yolo_outputs/           # Image assets for enrichment
├── requirements.txt            # Python dependencies
├── dbt_project.yml             # dbt config
└── .env (excluded from Git)    # Credentials for Telegram & DB
Secrets & Environment Handling: 
All credentials securely stored in .env:

env
TELEGRAM_API_ID=...
TELEGRAM_API_HASH=...
SESSION_NAME=...

POSTGRES_DB=...
POSTGRES_USER=...
POSTGRES_PASSWORD=...
Loaded via python-dotenv, excluded via .gitignore 

Progress & Deliverables (as of Task 2)
Task	Status	Summary
Task 0	Done	Git setup, Docker + environment config
Task 1	Done	Scraping & ingestion (400 messages loaded)
Task 2	Done	dbt star schema built, validated, tested
Task 3–5 Next	YOLO enrichment, FastAPI, orchestration
 Next Moves
 Run YOLOv8 on image_path assets to extract medical object metadata

 Build FastAPI endpoints: /top-products, /visual-content-ranking, etc.

 Automate full pipeline via Dagster for daily refresh

 Integrate semantic search (SentenceTransformers + ChromaDB)

Author
Sabona Terefe Machine Learning Engineer — NLP, Semantic Search GitHub: @sabonaterefe
