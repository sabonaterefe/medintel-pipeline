from dagster import op

@op
def scrape_telegram_data():
    # Your scrape logic
    return "scraped"
