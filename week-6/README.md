# Week 6 – Generative AI Programming Practical

## Objective

To evaluate the performance of a locally running Large Language Model (LLM) using Ollama and Python.

## Model Used

- Model: Llama 3.2
- Runtime: Ollama
- Release: v0.1

## Concepts Covered

- Local LLM execution using Ollama
- LLM API integration using Python
- JSON dataset handling
- Prompt execution
- Keyword-based evaluation
- Automated evaluation using Python
- CSV report generation

## Project Files

| File | Description |
|---|---|
| `main.py` | Python evaluation program |
| `golden_set.json` | Dataset containing 30 questions and expected answers |
| `requirements.txt` | Python dependencies |
| `baseline_results.csv` | Generated evaluation results |

## Evaluation Results

- Total Questions: 30
- Successful Responses: 30
- Passed: 12
- Review: 18
- Errors: 0
- Average Keyword Coverage: 48.89%
- Model: Llama 3.2
- Release: v0.1

## How to Run

1. Install Ollama.
2. Download the model using `ollama pull llama3.2`.
3. Install Python dependencies:

```bash
python -m pip install -r requirements.txt
```

4. Run the evaluation:

```bash
python main.py
```

5. View the generated `baseline_results.csv` file.

## Conclusion

Successfully implemented a local LLM evaluation system using Python and Ollama. The system evaluated 30 questions, calculated keyword coverage, classified responses as PASS or REVIEW, and generated a CSV evaluation report.