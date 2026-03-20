import requests
import json
import os

# Constants
OLLAMA_ENDPOINT = "http://localhost:11434/api/generate"
MODEL_NAME = "llama3.2:3b"

# List of 20 adapted e-commerce queries for Chic Boutique
queries = [
    "How do I use the referral program?",
    "How do I apply a discount code to my order?",
    "How do I check my order status?",
    "How do I see my recently viewed items?",
    "How do I upload a receipt for a return?",
    "How do I cancel my subscription?",
    "How do I update my shipping address?",
    "How do I change my account password?",
    "How do I add a new payment method?",
    "How do I set my preferred delivery time?",
    "How do I check my loyalty points balance?",
    "How do I remove an item from my cart?",
    "Where can I find my invoice?",
    "How do I connect my account to social media for rewards?",
    "How do I return a damaged item?",
    "How do I change the display currency?",
    "How do I add a gift message to my order?",
    "How do I enable two-factor authentication for my account?",
    "How do I check my membership privileges?",
    "Does Chic Boutique support international shipping?"
]

def query_ollama(prompt):
    """Sends a prompt to the Ollama API and returns the model response."""
    payload = {
        "model": MODEL_NAME,
        "prompt": prompt,
        "stream": False  # We want the full response at once
    }
    try:
        response = requests.post(OLLAMA_ENDPOINT, json=payload)
        response.raise_for_status() # Raise an exception for bad status codes
        # The actual response text is in the 'response' key of the JSON
        return response.json().get("response", "").strip()
    except requests.exceptions.RequestException as e:
        print(f"Error querying Ollama: {e}")
        return "Error: Could not get a response from the model."

def load_template(filepath):
    """Loads a prompt template from a file."""
    with open(filepath, 'r') as f:
        return f.read()

def main():
    # Load templates
    try:
        zero_shot_template = load_template("prompts/zero_shot_template.txt")
        one_shot_template = load_template("prompts/one_shot_template.txt")
    except FileNotFoundError as e:
        print(f"Error: Template file not found: {e}")
        return

    # Ensure evaluation directory exists
    os.makedirs("eval", exist_ok=True)

    print(f"Starting evaluation of {len(queries)} queries...")
    
    with open("eval/results.md", "w") as results_file:
        results_file.write("# Chatbot Evaluation Results: Zero-Shot vs One-Shot\n\n")
        
        for idx, query in enumerate(queries):
            print(f"Processing Query {idx + 1}/{len(queries)}: {query}")
            
            # 1. Zero-Shot
            zero_shot_prompt = zero_shot_template.format(query=query)
            zero_shot_response = query_ollama(zero_shot_prompt)
            
            # 2. One-Shot
            one_shot_prompt = one_shot_template.format(query=query)
            one_shot_response = query_ollama(one_shot_prompt)
            
            # Write to file
            results_file.write(f"## Query {idx + 1}: {query}\n\n")
            results_file.write(f"### Zero-Shot Response:\n{zero_shot_response}\n\n")
            results_file.write(f"### One-Shot Response:\n{one_shot_response}\n\n")
            results_file.write("---\n\n")
            
    print("Evaluation complete. Results saved to eval/results.md")

if __name__ == "__main__":
    main()
