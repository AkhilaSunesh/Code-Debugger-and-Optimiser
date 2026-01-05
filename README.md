# Project Title  
Code Debugging & Optimization Agent  

---

## Team Details  
- **Name:** Akhila Sunesh  
- **Institution:** Saintgits College of Engineering 

---

## Challenge Selected  
- ✅ **Code debugging & optimization agent**

---

## Problem Statement  
- Developers often struggle to quickly identify bugs and performance bottlenecks in code.  
- Manual debugging is time-consuming and requires deep expertise.  
- Beginners lack guidance on *why* code is inefficient.  
- Existing tools detect issues but rarely explain or optimize autonomously.  
- This solution targets **students, developers, and educators**.  

---

## Solution Overview  
- A **multi-agent AI system** that automatically debugs and optimizes Python code.  
- The system plans its approach, analyzes code, applies fixes, and evaluates results.  
- It is agentic because each agent independently makes decisions.  
- Key capabilities include bug detection, performance optimization, and explainable reasoning.  

---

## Agentic Design  

### Agents Involved  
- **Multiple agents**

### Role of Each Agent  
- **Planner Agent:** Determines the debugging and optimization strategy.  
- **Research Agent:** Identifies bugs, inefficiencies, and improvement opportunities.  
- **Coding Agent:** Applies fixes and optimizations to the code.  
- **Evaluation Agent:** Validates correctness and performance improvements.  

### Decision-Making & Autonomy  
- Agents operate sequentially without human intervention after task submission.  
- Each agent decides *what to do next* based on previous outputs.  

### Planning / Reasoning / Tool-Use Loops  
- Planning → Analysis → Action → Evaluation loop  
- No hardcoded logic paths; reasoning is LLM-driven.  

---

## Architecture Diagram  

<img width="1024" height="768" alt="Code Optimiser Flowchart (1)" src="https://github.com/user-attachments/assets/e5cbbad1-7d2a-4383-9324-6e12dd4ba081" />

---

## Components  

- **Frontend:** Streamlit  
- **Backend:** Python  
- **LLM(s) Used:** Google Gemini  
- **Tools / APIs:** Google GenAI SDK  
- **Vector DB / Memory:** None (stateless MVP)  

---

## Tech Stack  

- **Programming Language(s):** Python  
- **Frameworks / Libraries:** Streamlit, google-genai  
- **Models / APIs:** Gemini 2.5 Flash  
- **Database / Storage:** Not used  
- **Deployment:** Local / Streamlit Cloud  

---

## Features  

- Multi-agent autonomous code analysis  
- Automatic bug detection and optimization  
- Explainable agent reasoning  
- Clean, interactive UI  
- Secure API key handling  

---

## How to Run the Project  

### Prerequisites  
- Python 3.x  
- Gemini API Key  

### Installation  
```bash
git clone https://github.com/AkhilaSunesh/Code-Debugger-and-Optimiser.git
cd Code-Debugger-and-Optimiser
pip install -r requirements.txt
```

### Run
```bash
streamlit run app.py
```
App runs on: http://localhost:8501 <br>
Enter Gemini API key in the sidebar

## Demo

- **Demo Video Link (2 mins):** https://screenrec.com/share/pue1Uw5KcT
---

## Limitations & Future Work

### Known Limitations
- Supports only Python code  
- No runtime benchmarking in the current MVP  
- Stateless execution (no long-term memory between runs)  

### Future Enhancements
- Upload screenshots
- File upload support for `.py` files  
- Code diff visualization (before vs after)  

---

## Ethics, Safety & Responsible AI

- Avoids executing untrusted code directly  
- No storage of user code or API keys  
- Model outputs are advisory, not authoritative  
- Users are responsible for reviewing generated code  
- Designed for educational and development assistance







