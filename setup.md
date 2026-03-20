# Setup and Usage Guide: Offline Customer Support Chatbot

This guide explains how to set up and run the Chic Boutique customer support chatbot locally.

## Prerequisite: Ollama
1. Download and install Ollama from [ollama.com](https://ollama.com).
2. Ensure the Ollama server is running (check the tray icon or run `ollama serve`).

## 1. Model Preparation
Download the Llama 3.2 3B model:
```bash
ollama pull llama3.2:3b
```

## 2. Python Environment Setup
1. Create a virtual environment:
   ```bash
   python -m venv venv
   ```
2. Activate the virtual environment:
   - Windows: `.\venv\Scripts\activate`
   - macOS/Linux: `source venv/bin/activate`
3. Install dependencies:
   ```bash
   pip install requests datasets
   ```

## 3. Running the Chatbot
Run the evaluation script to process the queries:
```bash
python chatbot.py
```
This will:
- Load the templates from `prompts/`.
- Process 20 queries using Zero-Shot and One-Shot prompting.
- Save the results and responses to `eval/results.md`.

## 4. Project Structure
- `chatbot.py`: Core logic and API integration.
- `prompts/`: Contains `zero_shot_template.txt` and `one_shot_template.txt`.
- `eval/`: Contains `results.md` with evaluation outputs and scores.
- `report.md`: Detailed analysis of the project findings.
## 5. Offline vs. Online Access
- **Offline Core**: The `chatbot.py` script is **100% offline**. It connects directly to your local Ollama server (`localhost:11434`). You do NOT need internet to run the chatbot logic, query the model, or generate the results log.
- **Online Demo**: The `demo.py` script uses Gradio's `share=True` feature. This requires an internet connection ONLY to create a public tunnel (the `.gradio.live` link) so others can access your local chatbot remotely. 
- **Local-Only Demo**: To run the web interface without internet, simply set `share=False` in `demo.py`. It will only be accessible at `http://127.0.0.1:7860` on your machine.
