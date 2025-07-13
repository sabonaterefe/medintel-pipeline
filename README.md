MedIntel: ELT Pipeline for Ethiopian Medical Market Intelligence

Overview MedIntel is a modern ELT pipeline that extracts public Telegram content from Ethiopian medical vendors, transforms it into a queryable PostgreSQL warehouse, and enables insights through enrichment and API layers. It uses dbt for transformation and testing, with support for YOLOv8-based image analysis and FastAPI deployment.

Business Objectives

Identify frequently mentioned medical products and vendors

Compare content volume across Telegram channels

Track visual content trends using image flags

Analyze posting activity over time for market insights

Architecture Flow Telegram → JSON → PostgreSQL → dbt → YOLOv8 → FastAPI → Dagster

Tools per layer:

Extraction: Telethon

Loading: Python with psycopg2

Transformation: dbt and PostgreSQL

Testing: dbt tests and custom logic

Enrichment: YOLOv8 (prepped)

Serving: FastAPI (planned)

Orchestration: Dagster (planned)

Project Structure The dbt folder includes all models, tests, sources, and configuration:

dbt/models/staging: cleans raw messages (stg_telegram_messages.sql)

dbt/models/marts: final fact and dimension tables (fct_messages.sql, dim_channels.sql, dim_dates.sql)

dbt/tests: all validation tests (long_messages.sql, uniqueness, non-null checks)

dbt/schema.yml: source declarations and field descriptions

dbt_project.yml: updated config matching flattened structure

target/: compiled documentation (if included)

Other folders:

scripts/: scraping and loading logic

data/: raw and enriched assets

api/: FastAPI routes (optional setup)

dags/: Dagster orchestrations (planned)

README.md: complete project overview

Usage

Load Telegram data: python scripts/load_to_postgres.py

Run dbt transformations: dbt run

Test pipeline validity: dbt test

Generate documentation: dbt docs generate dbt docs serve

dbt Validation Summary

Models: staging, dimensions, fact

Tests:

Unique and not-null on keys

Custom length test (rejects empty/short messages)

Result: 13/13 tests passed

Profile: medintel_pipeline connected and verified

Documentation: lineage and schema served via dbt docs

Example Query Show message counts per channel: SELECT channel, COUNT(*) FROM staging.fct_messages GROUP BY channel ORDER BY COUNT DESC

Limitations & Next Steps

Currently limited to two channels (lobelia4cosmetics, tikvahpharma)

YOLOv8 image enrichment prepared but not applied

FastAPI endpoint not yet deployed

Semantic retrieval via ChromaDB planned

Dagster orchestration to be added

Author Sabona Terefe Machine Learning Engineer — NLP & Semantic Search GitHub: @sabonaterefe