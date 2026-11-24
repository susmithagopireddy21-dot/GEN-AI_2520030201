# Week 5 – Token Economics and Feature Budget Planning

## Aim

To understand token usage and estimate the cost of using an LLM application. This project also checks whether the planned usage fits within the available API limits and budget.

## Description

In this week, I created a Python program to calculate the expected token usage and cost of an LLM application.

The program calculates daily and monthly token usage, estimates the API cost, and checks RPM (Requests Per Minute) and TPM (Tokens Per Minute) limits.

It also includes a safety margin while checking the limits and budget. A separate program is used to test different usage scenarios.

## Files

- `budget.py` – Calculates token usage, daily and monthly costs, RPM and TPM capacity, and budget checks.
- `what_if.py` – Compares different usage scenarios, such as doubling requests, doubling input tokens, and reducing output tokens.
- `test_budget.py` – Contains unit tests to check cost calculations and capacity limits.
- `requirements.txt` – Contains the required Python package.
- `.env` – Stores the configuration values used by the program.
- `.gitignore` – Used to exclude unnecessary or private files.

## Concepts Covered

- Token Economics
- Input and Output Tokens
- Daily and Monthly Cost Estimation
- Requests Per Minute (RPM)
- Tokens Per Minute (TPM)
- API Usage Limits
- Safety Margin
- Feature Budget Planning
- What-if Analysis
- Python Unit Testing

## Installation

Install the required package:

```bash
pip install -r requirements.txt
```

## Running the Program

Run the main budget calculation:

```bash
python budget.py
```

Run the what-if analysis:

```bash
python what_if.py
```

Run the unit tests:

```bash
python -m unittest test_budget.py
```

## Expected Output

The main program displays:

- Input tokens per day
- Output tokens per day
- Total tokens per day
- Estimated daily cost
- Estimated monthly cost
- Peak RPM and TPM with safety margin
- Budget and capacity check results

The what-if analysis displays the cost and budget status for different usage scenarios.

## Learning Outcomes

Through this activity, I learned how to estimate LLM token usage, calculate API costs, check usage limits, and plan a feature within a given budget. I also understood how to use unit testing to verify the calculations.

## Conclusion

This activity helped me understand the importance of monitoring token usage and estimating API costs before building an LLM-based application. It also showed how different usage scenarios can affect the overall budget.