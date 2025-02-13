from flask import Flask, jsonify
import asyncio
from telegram_scraper import get_messages  # Import the get_messages function

app = Flask(__name__)

@app.route('/', methods=['GET'])
async def get_jobs():
    try:
        jobs = await get_messages()  # Await the async function
        if jobs:
            return jsonify(jobs), 200
        else:
            return jsonify({"message": "No jobs found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)  # Run the Flask app in debug mode
