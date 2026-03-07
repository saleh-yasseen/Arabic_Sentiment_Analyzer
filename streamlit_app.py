import streamlit as st
import requests
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="Arabic sentiment analyzer",page_icon="", layout="wide")
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
    api_status = "🟢 API is running"
except:
    api_status = "🔴 API offline(run fastapi dev main.py)"
st.sidebar.markdown(f"**API Status:** {api_status}")
tab1 , tab2 , tab3 = st.tabs(["Single Text", "Batch Processing", "Export Results"])
with tab1:
    st.header("Single Text Analysis")
    text_input = st.text_area(
        "Enter Arabic text for sentiment analysis:",
        height=150,
        placeholder="اكتب نصًا عربيًا هنا..."
    )
    col1, col2, col3 = st.columns([1,1,4])
    with col1:
        analyze_btn = st.button("analyze",type="primary")
    with col2:
        clear_btn = st.button("clear")
    if clear_btn:
        st.rerun()
    if analyze_btn:
        if not text_input.strip():
            st.warning("Please enter some Arabic text for analysis.")
        else:
            with st.spinner("analyzing..."):
                try:
                    response =requests.post(
                        f"{API_url}/analyze",
                        json={"text": text_input},
                        timeout=10
                    )

                    if  response.status_code == 200:
                        result =response.json()

                        sentiment = result['sentiment']
                        confidence = result['confidence']

                        if sentiment =="positive":
                            sentiment_class = "sentiment-positive"
                            emoji = "😊"
                            color = "#28a745"
                        elif sentiment =="negative":
                            sentiment_class = "sentiment-negative"
                            emoji = "😞"
                            color = "#dc3545"
                        else:
                            sentiment_class = "sentiment-neutral"
                            emoji = "😐"
                            color = "#ffc107"
                        
                        st.markdown(f'<div class="{sentiment_class}">', unsafe_allow_html=True)

                        col1, col2 = st.columns([1, 3])

                        with col1:
                            st.markdown(f"<h1 style='text-align: center;'>{emoji}</h1>", unsafe_allow_html=True)
                        with col2:
                            st.markdown(f"**Sentiment:**{sentiment}")
                            st.markdown(f"**confidence:**{confidence:.2%}")
                            if result.get('confident'):
                                st.success("The model is confident in its prediction.")
                            else:
                                st.warning("The model is not confident in its prediction.")
                        st.markdown("</div>", unsafe_allow_html=True)
                        st.progress(confidence)

                    else:
                        st.error(f"API error: {response.status_code}")

                except requests.exceptions.ConnectionError:
                    st.error("Failed to connect to the API. Please ensure the API is running.")
                except Exception as e:
                    st.error(f"An error occurred: {str(e)}")
with tab2:
    st.header("analyze multible texts")

    batch_input = st.text_area(
        "Enter multiple Arabic texts (one per line):",
        height =200,
        placeholder="اول نص\nثاني نص\nثالث نص"
    )
    col1, col2, col3 = st.columns([1,5])
    with col1:
        batch_btn = st.button("analyze batch",type="primary")
