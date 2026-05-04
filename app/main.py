import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import streamlit as st
import pandas as pd
from classifier import classify_email
from priority import get_priority
from summarizer import summarize_email

st.set_page_config(page_title="Smart Email Classifier", layout="wide")
st.title("Smart Email Classifier")

# Session state to track history
if "history" not in st.session_state:
    st.session_state.history = []

# --- Input section ---
email_input = st.text_area("Enter email content:", height=150)

if st.button("Analyze"):
    if email_input.strip():
        category = classify_email(email_input)
        priority = get_priority(email_input)
        summary = summarize_email(email_input)

        st.session_state.history.append({
            "Category": category,
            "Priority": priority,
            "Summary": summary,
            "Email": email_input[:80] + ("..." if len(email_input) > 80 else ""),
        })

        col1, col2 = st.columns(2)
        col1.metric("Category", category.upper())
        col2.metric("Priority", priority)

        st.subheader("Summary")
        st.info(summary)
    else:
        st.warning("Please enter some email content first.")

# --- Dashboard ---
if st.session_state.history:
    st.divider()
    st.subheader("Session Dashboard")

    df = pd.DataFrame(st.session_state.history)

    col1, col2 = st.columns(2)

    with col1:
        st.write("**Category Distribution**")
        cat_counts = df["Category"].value_counts()
        st.bar_chart(cat_counts)

    with col2:
        st.write("**Priority Distribution**")
        pri_counts = df["Priority"].value_counts()
        st.bar_chart(pri_counts)

    st.write("**Email History**")
    st.dataframe(df[["Category", "Priority", "Summary", "Email"]], use_container_width=True)

    if st.button("Clear History"):
        st.session_state.history = []
        st.rerun()
