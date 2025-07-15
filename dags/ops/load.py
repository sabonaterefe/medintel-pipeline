from dagster import op

@op
def load_raw_to_postgres(scrape_result):
    # You don't need scrape_result, but Dagster expects it
    # Your loading logic
    return "loaded"
