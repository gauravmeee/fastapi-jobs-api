from flask import Flask, jsonify
import asyncio
from telegram_scraper import get_messages  # Import the get_messages function

app = Flask(__name__)

@app.route('/', methods=['GET'])
def get_jobs():
    try:
        # Run the async function using asyncio
        jobs = asyncio.run(get_messages())
        
        if jobs:
            return jsonify(jobs), 200  # Return the jobs as a JSON response
        else:
            return jsonify({"message": "No jobs found"}), 404  # Handle empty results

    except Exception as e:
        return jsonify({"error": str(e)}), 500  # Handle any errors

if __name__ == '__main__':
    app.run(debug=True)  # Run the Flask app in debug mode
