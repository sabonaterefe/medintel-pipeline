## MedIntel: A Production-Grade ELT Pipeline for Ethiopian Medical Intelligence

Overview MedIntel is a scalable, validated ELT pipeline for transforming public Telegram content from Ethiopian medical vendors into a structured analytics warehouse. It’s built with modular components for ingestion, transformation, enrichment, and delivery.

This version includes:

Full dbt setup with model lineage and documented tests

Cleaned message pipeline with content validation

Source-aware schema configuration using schema.yml

Documentation generation via dbt docs

Optional image enrichment with YOLOv8 and API serving with FastAPI

## Business Questions Addressed

What products and medications are most commonly mentioned?

Which channels publish visual content most frequently?

How do posting volumes fluctuate daily or weekly?

## Architecture and Technology Stack Telegram → JSON → PostgreSQL → dbt → YOLOv8 → FastAPI → Dagster

Layer	Technologies
Extraction	Telethon
Loading	Python + psycopg2
Transformation	dbt
Validation	dbt tests
Enrichment	YOLOv8 (Task 3)
Serving	FastAPI (Task 4)
Orchestration	Dagster (Task 5)

## dbt Models and Lineage

Model	Description
raw.telegram_messages	Telegram-scraped source data
stg_telegram_messages	Cleans, trims, and filters messages using regex
dim_channels	Reference mapping for Telegram channels
dim_dates	Calendar dimension for time-based aggregation
fct_messages	Fact table combining content, image, and metadata
All models are declared and documented in schema.yml under models/staging.

## Test Coverage and Validation Summary

13 total tests implemented via dbt test:

not_null and unique checks on primary keys

Custom test: reject messages with length ≤ 1

All tests passed after cleaning pipeline logic

dbt logs confirm test success and model integrity

Custom filtering applied via: CHAR_LENGTH(REGEXP_REPLACE(TRIM(text), '\s+', '', 'g')) > 1

## Documentation Setup

Generated via:

dbt docs generate
dbt docs serve
Hosted locally at http://localhost:8080, includes:

Model descriptions

Column constraints

Source registry

Lineage graph

## Installation & Usage

Clone and spin up the pipeline:

git clone https://github.com/sabonaterefe/medintel-pipeline.git

cd medintel-pipeline

docker-compose up -d

Configure credentials in .env using python-dotenv

## Usage:

Run loader: python scripts/load_to_postgres.py

Run transformations: dbt run

Validate pipeline: dbt test

Visualize lineage: dbt docs serve

## Sample Query

sql
SELECT channel, COUNT(*) AS message_count
FROM staging.fct_messages
GROUP BY channel
ORDER BY message_count DESC;

## Limitations

Currently supports two channels: lobelia4cosmetics, tikvahpharma

YOLO enrichment pipeline staged but not yet executed

Semantic search integration with ChromaDB in planning stage

## Future Work

Apply YOLOv8 to enrich image-linked messages

Serve filtered insights via FastAPI endpoints

Add Dagster orchestration pipelines

Implement semantic search and clustering

## Author

Sabona Terefe Machine Learning Engineer | NLP | Semantic Search GitHub: @sabonaterefe
