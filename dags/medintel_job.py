from dagster import job
from dags.ops.scrape import scrape_telegram_data
from dags.ops.load import load_raw_to_postgres
from dags.ops.transform import run_dbt_transformations
from dags.ops.enrich import run_yolo_enrichment

@job
def medintel_pipeline():
    scraped = scrape_telegram_data()
    loaded = load_raw_to_postgres(scraped)
    transformed = run_dbt_transformations(loaded)
    run_yolo_enrichment(transformed)
