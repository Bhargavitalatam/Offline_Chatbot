# Project Report: Offline Customer Support Chatbot (Chic Boutique)

## 1. Introduction
The objective of this project was to evaluate the feasibility of deploying a local Large Language Model (LLM) for automated customer support. By using Ollama and Meta's Llama 3.2 3B model, we aimed to build a functional chatbot that ensures data privacy and eliminates API costs. The experiment specifically compared two fundamental prompting techniques: Zero-Shot and One-Shot prompting.

## 2. Methodology
- **Model**: Llama 3.2 (3B), quantized for local efficiency.
- **Dataset**: 20 customer queries adapted from the Ubuntu Dialogue Corpus to fit an e-commerce context (Chic Boutique).
- **Prompting**: 
    - **Zero-Shot**: Role assignment ("Chic Boutique agent") and query.
    - **One-Shot**: Role assignment, one high-quality example (Return Policy), and query.
- **Scoring Rubric**: Manual evaluation (1-5 scale) for Relevance, Coherence, and Helpfulness.

## 3. Results & Analysis
### 3.1 Score Summary
| Method | Avg Relevance | Avg Coherence | Avg Helpfulness |
| :--- | :--- | :--- | :--- |
| **Zero-Shot** | **4.85** | **5.0** | **4.75** |
| **One-Shot** | 4.55 | 5.0 | 4.15 |

### 3.2 Observations
- **Coherence**: Llama 3.2 3B demonstrated flawless coherence. Every response followed proper grammar and a professional, friendly tone.
- **Zero-Shot Performance**: Counter-intuitively, Zero-Shot outperformed One-Shot in this specific setup. The model was highly capable of inferring the persona and providing detailed (though potentially hallucinated) UI paths for users.
- **One-Shot Limitations**: The One-Shot prompt occasionally caused the model to be more "defensive" or concise. In some cases, if the query was slightly outside the scope of the provided example, the model defaulted to "I am not aware" or very vague responses (e.g., Query 15 & 16), whereas Zero-Shot provided a more helpful (if prescriptive) path.
- **Examples**:
    - *Good (Zero-Shot)*: Query 1 (Referral Program) provided a 5-step guide that was perfectly structured.
    - *Weak (One-Shot)*: Query 18 (2FA) responded with "I'm not sure", failing to offer the helpful alternate paths that the Zero-Shot response provided.

## 4. Conclusion & Limitations
### Conclusion
Llama 3.2 3B is highly suitable for generating professional customer support responses offline. It captures tone and intent excellently. It is effective for answering general policy questions and providing a first layer of support.

### Limitations
- **Hallucination**: The model assumes specific UI elements (e.g., "Actions button", "Rewards & Loyalty tab") that may not exist in the real store.
- **Static Knowledge**: Without RAG (Retrieval-Augmented Generation), the model doesn't have access to real-time order data or fluctuating product availability.
- **Scale**: While 3B is fast, it occasionally misses the nuance that a larger model (70B) might capture in complex multi-step instructions.
- **Hardware Dependency**: Performance was measured on a local machine; response times are subject to CPU/GPU availability, as is typical for local inference.

### Next Steps
1. **RAG Integration**: Provide the model with a real knowledge base (FAQ/Policy documents) to reduce hallucination.
2. **System Integration**: Connect the chatbot to an order tracking API to provide real-time status updates.
3. **Few-Shot refinement**: Use multiple examples instead of just one to better define the response boundaries.

## 5. Setup Documentation
Refer to `setup.md` for instructions on reproducing this environment.
