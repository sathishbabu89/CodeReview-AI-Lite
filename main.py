import streamlit as st
from review_engine import llm_suggestion, run_static_analysis

st.title("🧠 Code Review Assistant (Lite)")
code_input = st.text_area("Paste your Python code here", height=200)

if st.button("Run Review"):
    if code_input:
        st.markdown("### 🤖 LLM Suggestions")
        st.success(llm_suggestion(code_input))

        st.markdown("### 🧪 Static Analysis")
        result = run_static_analysis(code_input)
        st.code(result)
    else:
        st.warning("Please paste some code to review.")
