import streamlit as st
import requests
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="Arabic sentiment analyzer", layout="wide")
st.markdown("""
<style>
    .main-header {
        font-size:3rem;
        color: #4A90E2;
        text-align: center;
        margin-bottom: 2rem;
    }
    .sentiment-positive{
        background-color: #d4edda;
        border-left: 5px solid #28a745;
        padding: 1rem;
        border-radius: 5px;
    }
    .sentiment-negative{
        background-color: #f8d7da;
        border-left: 5px solid #dc3545;
        padding: 1rem;
        border-radrius: 5px;   
    }
    .sentiment-neutral{
        background-color: #fff3cd;
        border-left: 5px solid #ffc107;
        padding: 1rem;
        border-radius: 5px;   
    }
</style>
""", unsafe_allow_html=True)

st.markdown('<h1 class="main-header">Arabic Sentiment Analyzer</h1>', unsafe_allow_html=True)
st.markdown("___")

with st.sidebar:
    st.header("About")
    st.info(
        """
        This app analyzes sentiment in Arabic text using a fine-tuned BERT model.
        
        **Model:** CAMeL-Lab BERT  
        **Classes:** Positive, Negative, Neutral  
        **Accuracy:** ~87%
        """
    )
    
    st.header("🛠️ Features")
    st.markdown("""
    - Single text analysis
    - Batch processing
    - Confidence scores
    - Export results
    """)
    
    st.header("📞 Contact")
    st.markdown("""
    - [GitHub](https://github.com/saleh-yasseen)
    - [LinkedIn](https://www.linkedin.com/in/saleh-yassien-b16256202/)
    """)

API_url ="http://localhost:8000"

try:
    response = requests.get(API_url,timeout=2)
    api_status = "API is running"
except:
    api_status = "API offline(run fastapi dev main.py)"
st.sidebar.markdown(f"**API Status:** {api_status}")
tab1 , tab2 , tab3 = st.tabs(["Single Text", "Batch Processing", "Export Results"])
with tab1:
    st.header("Single Text Analysis")
    text_input = st.text_area(
        "Enter Arabic text for sentiment analysis:",
        height=150,
        placeholder="اكتب نصًا عربيًا هنا..."
    )
    
