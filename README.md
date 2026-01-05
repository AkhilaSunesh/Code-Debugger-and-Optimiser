# Code-Debugger-and-Optimiser Agent

A **multi-agent autonomous system** that analyzes, debugs, and optimizes Python code using **LLM-powered agents** following a structured pipeline:

> **Planner → Research → Coding → Evaluation**

Built with **Streamlit** and **Google Gemini**, this project demonstrates how agent-based AI systems can autonomously reason, act, and self-evaluate.

---

## 🚀 Features

- 🔍 Automatic bug detection
- ⚡ Performance optimization
- 🧠 Multi-agent reasoning pipeline
- 📊 Step-by-step explainability
- 🧼 Clean, minimal Streamlit UI
- 🔐 Secure API key handling

---

## 🧩 Architecture
<img width="1024" height="768" alt="Code Optimiser Flowchart (1)" src="https://github.com/user-attachments/assets/745de905-cb0d-4182-9f20-c203d9f39873" />


Each agent has a **single responsibility**, making the system modular, explainable, and extensible.

---

## 🤖 Why This Is Autonomous

Once the user submits the code and task:

- The **Planner Agent** decides the debugging strategy
- The **Research Agent** identifies bugs and inefficiencies
- The **Coding Agent** applies fixes and optimizations
- The **Evaluation Agent** validates correctness and improvements

No further human input is required.

> This makes the system a **semi-autonomous agent pipeline** — human-defined goal, autonomous execution.

---

## 🛠️ Tech Stack

- **Python**
- **Streamlit** – UI
- **Google Gemini (google-genai SDK)** – LLM
- **Multi-agent architecture**

---

## ⚙️ Installation & Setup

### Clone the repository
```bash
git clone https://github.com/AkhilaSunesh/Code-Debugger-and-Optimiser.git
cd Code-Debugger-and-Optimiser
```
### Install dependencies
```bash
pip install -r requirements.txt
```

### Run the app
```bash
streamlit run app.py
```
## Example Test Code
```python
def slow_sum(n):
    result = 0
    for i in range(n):
        for j in range(n):
            result += i + j
    return result
```
## Future Enhancements
- Feature to upload Screenshots
- Feature to upload files (with .py extension)

## Google Colab
https://colab.research.google.com/drive/1rfXzkSkKddwfVewPmJRGQDQE2S2OJmPZ?usp=sharing
  



