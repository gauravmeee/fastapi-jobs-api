import os
from telethon import TelegramClient

# Load API credentials from environment variables
api_id = os.getenv("TELEGRAM_API_ID")  
api_hash = os.getenv("TELEGRAM_API_HASH")  

# Create the client session
client = TelegramClient('session_name', api_id, api_hash)

async def main():
    await client.start()  # This will prompt for your phone number & OTP
    print("Logged in successfully!")

with client:
    client.loop.run_until_complete(main())
