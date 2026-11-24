# Week 3 – LLM Usage Monitoring and Cost Tracking

## Objective

To monitor Large Language Model (LLM) usage by tracking tokens, response time, estimated API cost, and storing usage details in MongoDB.

## Concepts Covered

- LLM provider integration using Gemini and Ollama
- Input and output token tracking
- Total token calculation
- Response latency measurement
- Estimated API cost calculation
- MongoDB database connectivity
- Usage logging and timestamp recording
- Retry handling for temporary errors
- Unit testing using a fake provider and logger

## Files

- `main.py` – Main program that allows the user to choose Gemini or Ollama, enter a prompt, and display the response.
- `llm_client.py` – Contains the LLM providers and client logic for generating responses, tracking tokens, measuring latency, estimating cost, and handling retries.
- `usage_logger.py` – Connects to MongoDB and stores API usage records in the database.
- `test_client.py` – Tests LLM response generation and verifies that usage details are logged correctly.
- `requirements.txt` – Contains the Python libraries required for the project.
- `.env` – Stores API keys, MongoDB connection details, and pricing configuration.
- `.gitignore` – Prevents sensitive files and unnecessary Python files from being tracked by Git.

## Technologies Used

- Python
- Google Gemini API
- Ollama (Llama 3.2)
- MongoDB
- PyMongo
- Python dotenv
- Requests
- Unittest

## Setup and Installation

1. Create and activate a Python virtual environment.

2. Install the required packages:

```bash
pip install -r requirements.txt
```

3. Configure the required environment variables in the `.env` file:

```env
GEMINI_API_KEY=your_gemini_api_key
MONGODB_URI=your_mongodb_connection_string
GEMINI_INPUT_PRICE_PER_MILLION=your_input_price
GEMINI_OUTPUT_PRICE_PER_MILLION=your_output_price
```

4. Make sure MongoDB is accessible using the connection string.

5. If using Ollama, make sure Ollama is running and the `llama3.2` model is available.

## Running the Program

Run the following command:

```bash
python main.py
```

Choose the provider when prompted:

- `gemini` – Uses the hosted Gemini API.
- `ollama` – Uses the locally running Ollama model.

Enter a question and the program generates an LLM response.

## Usage Monitoring

After generating a response, the program tracks:

- Provider and model name
- Input tokens
- Output tokens
- Total tokens
- Response latency in milliseconds
- Estimated cost in USD
- Request status
- Number of attempts

For Gemini, the estimated cost is calculated using the configured input and output token prices.

For local Ollama inference, the hosted API token charge is recorded as zero. Local inference costs are not included.

## MongoDB Storage

The program connects to the MongoDB database named `llm_monitoring` and stores usage records in the `api_usage` collection.

Each usage record includes a UTC timestamp. The logger also retries failed database writes up to three times.

## Testing

Run the unit test using:

```bash
python -m unittest test_client.py
```

The test uses a fake provider and fake logger to verify response generation and usage logging without making a real LLM API call.

## Result

Successfully developed an LLM usage monitoring system that supports Gemini and Ollama, tracks token usage and response latency, estimates hosted API costs, and stores usage records in MongoDB.