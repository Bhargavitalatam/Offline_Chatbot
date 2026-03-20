import gradio as gr
import requests
import json

# Constants
OLLAMA_ENDPOINT = "http://localhost:11434/api/generate"
MODEL_NAME = "llama3.2:3b"

def query_ollama(message, history):
    """Sends a message to the Ollama API and returns the model response."""
    # Use the Zero-Shot template for the demo
    template = "You are a helpful, friendly, and concise customer support agent for an online store called 'Chic Boutique'. Your goal is to assist customers with their questions. Do not make up information about policies if you don't know the answer.\n\nCustomer Query: \"{query}\"\n\nAgent Response:"
    
    prompt = template.format(query=message)
    
    payload = {
        "model": MODEL_NAME,
        "prompt": prompt,
        "stream": False
    }
    
    try:
        response = requests.post(OLLAMA_ENDPOINT, json=payload)
        response.raise_for_status()
        return response.json().get("response", "").strip()
    except Exception as e:
        return f"Error connecting to Ollama: {e}. Please ensure Ollama is running locally."

# Create Gradio UI
demo = gr.ChatInterface(
    fn=query_ollama, 
    title="Chic Boutique - Offline Customer Support Demo",
    description="Ask anything about our products, returns, or shipping! (Powered by Llama 3.2 3B)",
    examples=["How do I track my order?", "What is your return policy?", "How do I use a discount code?"]
)

if __name__ == "__main__":
    print("Launching Offline Web UI...")
    print("Access the chatbot locally at: http://127.0.0.1:7860")
    # share=False ensures no internet connection or tunnel is required.
    demo.launch(share=False)
