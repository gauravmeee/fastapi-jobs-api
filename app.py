from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import asyncio
from telegram_scraper import get_messages

app = FastAPI()

# Allow CORS for all origins (You can restrict it by modifying the origins list)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins, you can specify your frontend URL here
    allow_credentials=True,
    allow_methods=["*"],  # Allows all HTTP methods
    allow_headers=["*"],  # Allows all headers
)

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
