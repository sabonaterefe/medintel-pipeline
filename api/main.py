from fastapi import FastAPI
from api.crud import top_products, channel_activity, search_messages

app = FastAPI()

@app.get("/api/reports/top-products")
def top_products_endpoint(limit: int = 10):
    return top_products(limit)

@app.get("/api/channels/{channel_name}/activity")
def activity_endpoint(channel_name: str):
    return channel_activity(channel_name)

@app.get("/api/search/messages")
def search_endpoint(query: str):
    return search_messages(query)
