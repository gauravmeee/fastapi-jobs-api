from fastapi import FastAPI
import asyncio
from telegram_scraper import get_messages

app = FastAPI()

@app.get("/")
async def get_jobs():
    try:
        jobs = await get_messages()  # Use await for async function
        if jobs:
            return jobs
        else:
            return {"message": "No jobs found"}
    except Exception as e:
        return {"error": str(e)}
