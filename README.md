## MedIntel: ELT Pipeline for Ethiopian Medical Market Intelligence

## Overview

MedIntel is a data pipeline designed to extract and transform content from public Telegram channels related to Ethiopian medical vendors. It uses the dbt framework to clean, validate, and document the data before storing it in a PostgreSQL warehouse. Image enrichment and semantic search extensions are planned.

## Core Objectives

Monitor product mentions and channel activity

Structure raw message data for analysis

Validate data integrity using dbt tests

Serve visual proof of dbt setup and lineage

## Project Structure

medintel-pipeline/
├── dbt/
│   ├── models/
│   │   ├── staging/
│   │   │   └── stg_telegram_messages.sql
│   │   ├── marts/
│   │   │   ├── fct_messages.sql
│   │   │   ├── dim_channels.sql
│   │   │   └── dim_dates.sql
│   ├── tests/
│   │   └── long_messages.sql
│   ├── schema.yml
│   └── dbt_project.yml
├── docs/
│   ├── lineage_graph.png
│   ├── test_results.png
│   └── run_summary.md
All dbt models, tests, and configs are located in the dbt/ folder.  Visual confirmation exists in the docs/ folder.

## dbt Implementation Details

Project name: medintel_pipeline

Profile name: medintel_pipeline — validated with dbt debug

Models built: 4 view models (staging and marts)

## Tests implemented: 13 total

Includes not_null, unique, and a custom content-length check

Execution confirmed:

dbt run completed successfully

dbt test passed all validations

dbt docs generate created model lineage and documentation

## Evidence of Implementation

See docs/ folder for:

lineage_graph.png — dbt lineage screenshot

test_results.png — visual of 13/13 test pass summary

run_summary.md — summary of dbt execution and result status

## Sample Query

sql
SELECT channel, COUNT(*) 
FROM staging.fct_messages 
GROUP BY channel 
ORDER BY COUNT DESC;
## Limitations

Data includes only two channels: lobelia4cosmetics and tikvahpharma

YOLOv8 image enrichment is prepared but not yet applied

FastAPI serving and Dagster orchestration are planned

Semantic search via ChromaDB is on the roadmap

## Author

Sabona Terefe Machine Learning Engineer specializing in NLP and Semantic Search GitHub: @sabonaterefe