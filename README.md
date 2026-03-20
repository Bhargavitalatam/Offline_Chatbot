# Offline Customer Support Chatbot

A functional offline customer support chatbot built with Ollama and Llama 3.2.

## Project Overview
This project demonstrates how to deploy and interact with Large Language Models (LLMs) locally, ensuring data privacy and eliminating API costs. It focuses on prompt engineering (Zero-shot vs. One-shot) and performance evaluation for an e-commerce customer support use case.

## Tech Stack
- **Model**: Meta Llama 3.2 (3B)
- **Inference Server**: Ollama
- **Language**: Python
- **Libraries**: `requests`, `datasets`

## Directory Structure
- `prompts/`: Prompt templates for zero-shot and one-shot interactions.
- `eval/`: Evaluation results and logs.
- `chatbot.py`: Main interaction script.
- `setup.md`: Technical documentation of the setup process.
- `report.md`: Project findings and evaluation results.
- `README.md`: Project overview.

## Live Demo
Check out the interactive demo here: [Chic Boutique Chatbot (Gradio)](https://1af0e33525799eaa0d.gradio.live)
*(Link expires in 7 days)*

## Setup
Refer to `setup.md` for detailed environment configuration.

## FAQ
**Q: The Ollama server isn't responding or I'm getting a connection error.**
A: Ensure the Ollama application is running (check system tray). Confirm you are sending requests to `http://localhost:11434`.

**Q: The model's responses are very slow. Is this normal?**
A: Yes, this is expected when running an LLM on a CPU locally. performance depends heavily on your hardware.

**Q: Can I use a different model?**
A: Yes. Run `ollama pull <model_name>` and update the `MODEL_NAME` constant in `chatbot.py`.
