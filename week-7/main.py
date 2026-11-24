
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

# Step 1: Select the model
MODEL_NAME = "distilgpt2"

print("Loading model...")

# Step 2: Load tokenizer and model
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForCausalLM.from_pretrained(MODEL_NAME)

# Step 3: Give an input prompt
prompt = "Artificial Intelligence is"

print("\nInput Prompt:", prompt)

# Step 4: Convert prompt into token IDs
inputs = tokenizer(prompt, return_tensors="pt")

# Step 5: Get model output
with torch.no_grad():
    outputs = model(**inputs)

# Step 6: Extract logits for the next token
logits = outputs.logits[:, -1, :]

# Step 7: Convert logits into probabilities
probabilities = torch.softmax(logits, dim=-1)

# Step 8: Find top 5 probable next tokens
top_k = 5

top_probabilities, top_token_ids = torch.topk(
    probabilities, top_k, dim=-1
)

# Step 9: Display results
print("\nTop", top_k, "Next-Token Predictions:")
print("-" * 65)

for i in range(top_k):
    token_id = top_token_ids[0, i].item()
    token = tokenizer.decode([token_id])
    probability = top_probabilities[0, i].item()
    logit = logits[0, token_id].item()

    print(
        f"{i + 1}. Token: {repr(token):15} "
        f"ID: {token_id:6} "
        f"Logit: {logit:10.4f} "
        f"Probability: {probability:.6f}"
    )

print("\nExperiment completed successfully!")
