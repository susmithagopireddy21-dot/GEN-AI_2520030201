# Week 2 – Provider-Agnostic LLM Client

## Objective
In this practical, I learned how to connect different LLM providers using a single common interface. I worked with Gemini API and Ollama (Llama 3.2) to understand how both cloud-based and locally running models can be used in a Python application.

## What I Learned
- Understood what a provider-agnostic LLM client means.
- Learned how to work with the Gemini API.
- Installed and used Ollama on my local system.
- Downloaded and worked with the Llama 3.2 model.
- Learned how to create a common interface for different LLM providers.
- Understood how to send prompts and receive responses from different models.
- Learned the basics of testing Python programs using unit tests.

## Files Used
- `llm_client.py` – Contains the common interface and provider classes for Gemini and Ollama.
- `main.py` – Allows me to select a provider, enter a prompt and get the LLM response.
- `test_client.py` – Used to test the LLM client with a fake provider.
- `requirements.txt` – Contains the Python libraries needed for this practical.
- `.env` – Used to store the Gemini API key securely.
- `.gitignore` – Helps prevent sensitive and unnecessary files from being uploaded to GitHub.

## Steps to Run the Program

First, I installed Ollama and downloaded the Llama 3.2 model. Then I installed the required Python packages and ran the program.

```bash
ollama pull llama3.2
pip install -r requirements.txt
python main.py
```

While running the program, I can choose either Gemini or Ollama as the provider and enter my question to get a response.

## Learning Outcome
After completing this practical, I understood how to use two different LLM providers through a common client. I also learned how to work with local language models, connect to a hosted API and test the client using Python.

## Conclusion
This practical helped me understand how different LLM providers can be used in the same application. I also got practical experience with Gemini, Ollama and Llama 3.2.