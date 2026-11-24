
# Week 7 – Next-Token Probability Analysis Using Hugging Face Transformers

## Objective

To inspect the next-token predictions of a small open language model using Hugging Face Transformers and understand logits, probabilities, and top-k token candidates.

## Concepts Covered

- Large Language Models (LLMs)
- Hugging Face Transformers
- Tokenization
- Token IDs
- Next-token prediction
- Logits
- Softmax function
- Probability distribution
- Top-k candidate selection
- PyTorch

## Tools and Technologies

- Python
- PyTorch
- Hugging Face Transformers
- DistilGPT-2

## Files

- `main.py` – Loads the model, processes the input prompt, calculates logits and probabilities, and displays the top 5 next-token candidates.
- `requirements.txt` – Contains the required Python libraries.

## Installation

Install the required dependencies using:

```bash
python -m pip install -r requirements.txt
```

## Execution

Run the Python program using:

```bash
python main.py
```

The program loads the DistilGPT-2 model and processes the prompt:

`Artificial Intelligence is`

It then displays the top 5 predicted next tokens with their token IDs, logits, and probabilities.

## Sample Output

```text
Input Prompt: Artificial Intelligence is

Top 5 Next-Token Predictions:

1. Token: ' a'    ID: 257
   Logit: -58.4307
   Probability: 0.213057

2. Token: ' the'  ID: 262
   Logit: -59.3685
   Probability: 0.083410

3. Token: ' an'   ID: 281
   Logit: -59.9070
   Probability: 0.048677

4. Token: ' not'  ID: 407
   Logit: -60.1266
   Probability: 0.039083

5. Token: ' one'  ID: 530
   Logit: -60.1712
   Probability: 0.037376

Experiment completed successfully!
```

## Result

Successfully loaded the DistilGPT-2 model using Hugging Face Transformers, extracted next-token logits, converted them into probabilities using the softmax function, and displayed the top 5 next-token candidates.

## Conclusion

This experiment demonstrates how a language model predicts the next token based on an input prompt. It provides practical understanding of logits, probability distributions, and top-k token selection.
