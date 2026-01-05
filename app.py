import os
import streamlit as st
from google import genai

# -----------------------
# Page Config
# -----------------------
st.set_page_config(
    page_title="Code Debugging & Optimization Agent",
    page_icon="🧠",
    layout="wide"
)

# -----------------------
# Sidebar – API Key
# -----------------------
st.sidebar.title("🔑 Configuration")

api_key = st.sidebar.text_input(
    "Enter GEMINI API Key",
    type="password"
)

if api_key:
    os.environ["GEMINI_API_KEY"] = api_key

# -----------------------
# Initialize Client
# -----------------------
def get_client():
    return genai.Client(api_key=os.environ["GEMINI_API_KEY"])

def send_chat(prompt):
    client = get_client()
    chat = client.chats.create(model="gemini-2.5-flash")
    response = chat.send_message(prompt)
    return response.text

# -----------------------
# Agents
# -----------------------
def planner_agent(task):
    prompt = f"""
    You are a Planner Agent.
    Break down this debugging task into steps for Research, Coding, and Evaluation agents.
    Task: {task}
    """
    return send_chat(prompt)

def research_agent(plan, code):
    prompt = f"""
    You are a Research Agent.
    Based on the plan below, analyze the code for bugs and inefficiencies.

    Plan:
    {plan}

    Code:
    {code}
    """
    return send_chat(prompt)

def coding_agent(research, code):
    prompt = f"""
    You are a Coding Agent.
    Apply fixes and optimizations based on the research.

    Research:
    {research}

    Original Code:
    {code}

    Output only optimized Python code.
    """
    return send_chat(prompt)

def evaluation_agent(original, optimized):
    prompt = f"""
    You are an Evaluation Agent.
    Compare original and optimized code for correctness and performance.

    Original:
    {original}

    Optimized:
    {optimized}
    """
    return send_chat(prompt)

# -----------------------
# Main UI
# -----------------------
st.title("🧠 Code Debugging & Optimization Agent")
st.caption("Planner → Research → Coding → Evaluation")

col1, col2 = st.columns(2)

with col1:
    st.subheader("📥 Input Code")
    user_code = st.text_area(
        "Paste your Python code here",
        height=300,
        placeholder="def example():\n    pass"
    )

with col2:
    st.subheader("🎯 Task Description")
    task_desc = st.text_area(
        "What should the agent do?",
        value="Debug and optimize this Python code for performance and correctness."
    )

run_btn = st.button("🚀 Analyze & Optimize", use_container_width=True)

# -----------------------
# Run Agents
# -----------------------
if run_btn:
    if not api_key:
        st.error("Please enter your GEMINI API Key.")
    elif not user_code.strip():
        st.error("Please provide some code.")
    else:
        with st.spinner("Planner Agent working..."):
            plan = planner_agent(task_desc)

        with st.spinner("Research Agent analyzing..."):
            research = research_agent(plan, user_code)

        with st.spinner("Coding Agent optimizing..."):
            optimized = coding_agent(research, user_code)

        with st.spinner("Evaluation Agent evaluating..."):
            evaluation = evaluation_agent(user_code, optimized)

        # -----------------------
        # Results Tabs
        # -----------------------
        tabs = st.tabs([
            "📌 Planner",
            "🔍 Research",
            "💻 Optimized Code",
            "✅ Evaluation"
        ])

        with tabs[0]:
            st.markdown(plan)

        with tabs[1]:
            st.markdown(research)

        with tabs[2]:
            st.code(optimized, language="python")

        with tabs[3]:
            st.markdown(evaluation)
