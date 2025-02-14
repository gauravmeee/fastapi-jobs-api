import re
import json
from telethon import TelegramClient
import os

# Load credentials from environment variables
api_id = os.getenv("TELEGRAM_API_ID")  
api_hash = os.getenv("TELEGRAM_API_HASH")  

client = TelegramClient('session_name', api_id, api_hash)

async def get_messages():
    await client.start()
    
    try:
        channel = await client.get_entity('jobs_and_internships_updates')
        messages = await client.get_messages(channel, limit=100)  # Fetch latest 100 messages

        jobs = []

        for message in messages:
            if not message.text:
                continue

            # Remove lines starting with "Community" "for latest Jobs & Intenrship Updates" and "lintr.ee"
            text = re.sub(r"Community.|for Latest Jobs & Internships Updates|Share with your College Whatsapp Groups & Friends too|https://linktr.ee.*", "", message.text, flags=re.IGNORECASE).strip()
            
             # Normalize text
            text = re.sub(r'\s+', ' ', text).strip()  

            job_data = {
                "company": re.search(r"Company\s*Name:\s*(.+?)\s*(?:Role|Batch|Location|Apply)", text, re.IGNORECASE),
                "role": re.search(r"Role:\s*(.+?)\s*(?:Batch|Location|Apply)", text, re.IGNORECASE),
                "batch_eligible": re.search(r"Batch\s*Eligible:\s*(.+?)(?:Location|Apply|Expected Stipend|Expected Benefits|$)", text, re.IGNORECASE),
                "location": re.search(r"Location:\s*(.+?)\s*(?:Apply|Expected)", text, re.IGNORECASE),
                "apply_link": re.search(r"Apply\s*Link:\s*(https?://[^\s]+)", text, re.IGNORECASE),
                "expected_ctc": re.search(r"Expected\s*CTC:\s*(.+?)\s*(?:Expected Stipend|Apply|Expected Benefits|$)", text, re.IGNORECASE),
                "expected_stipend": re.search(r"Expected\s*Stipend:\s*(.+?)\s*(?:Apply|Expected Benefits|Expected CTC|$)", text, re.IGNORECASE),
                "expected_benefits": re.search(r"Expected\s*Benefits:\s*(.+?)\s*(?:Apply|Expected CTC|$)", text, re.IGNORECASE),
                "date_posted": message.date.strftime('%Y-%m-%d %H:%M:%S')  # Format the date of posting
            }

            # Convert MatchObject to string (handling None cases)
            for key, match in job_data.items():
                if match:
                    job_data[key] = match.group(1).strip() if hasattr(match, 'group') else match
                else:
                    job_data[key] = None
            
            # Store only if essential fields are found
            if job_data["company"] and job_data["role"] and job_data["batch_eligible"] and job_data["location"] and job_data["apply_link"]:
                jobs.append(job_data)

        return jobs  # Return the jobs list instead of printing it

    except Exception as e:
        print(f"Error: {e}")
        return []  # Return an empty list in case of error

# To run here 
import asyncio

# Make sure the code below is wrapped in an asynchronous entry point
async def main():
    jobs = await get_messages()
    print(json.dumps(jobs, indent=4))

if __name__ == "__main__":
    asyncio.run(main())  # To execute the async code from the main thread

