# Telegram Job Scraper API

This project provides a FastAPI-based service that scrapes job and internship updates from a Telegram channel. The scraped data is returned as a JSON response.

## Features
- **Scrapes Telegram messages** from the "jobs_and_internships_updates" channel.
- Extracts job-related details such as company, role, batch eligibility, location, application link, expected CTC, stipend, and benefits.
- **CORS enabled** for cross-origin requests, useful for front-end integrations.
- Asynchronous scraping with `Telethon` and `FastAPI`.

## Installation

### Prerequisites

Ensure you have Python 3.7+ installed and the following packages:

1. `fastapi` - Web framework.
2. `uvicorn` - ASGI server to run the FastAPI app.
3. `telethon` - Library to interact with Telegram API.

You can install the required dependencies by running:

```bash
pip install fastapi uvicorn telethon
```

### Telegram Credentials

You will need a **Telegram API ID** and **API hash** to access Telegram's API.

1. Go to [my.telegram.org](https://my.telegram.org).
2. Log in with your phone number.
3. Under "API development tools", create a new application.
4. Copy the **API ID** and **API Hash** and set them as environment variables:

```bash
export TELEGRAM_API_ID="your_api_id"
export TELEGRAM_API_HASH="your_api_hash"
```

### Running the Server

To run the FastAPI application locally, use `uvicorn`:

```bash
uvicorn app:app --reload
```

This will start the server at `http://127.0.0.1:8000`. You can now make a GET request to `http://127.0.0.1:8000/` to retrieve job information.

### API Endpoint

- **GET `/`**: Fetches job and internship updates from the Telegram channel as JSON.

### Example Response:

```json
[
  {
    "company": "XYZ Corp",
    "role": "Software Engineer",
    "batch_eligible": "2023-2025",
    "location": "Remote",
    "apply_link": "https://xyz.com/apply",
    "expected_ctc": "12 LPA",
    "expected_stipend": "10,000 INR",
    "expected_benefits": "Health Insurance"
  },
  ...
]
```

## Code Structure

- `app.py`: FastAPI application with the `/` endpoint.
- `telegram_scraper.py`: Contains the scraping logic using `Telethon` to fetch messages from the Telegram channel.

## Contributing

Feel free to fork this project, open issues, and submit pull requests for improvements.

## License

This project is licensed under the MIT License.
