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
    col1, col2 = st.columns([1,5])
    with col1:
        batch_btn = st.button("analyze batch",type="primary")

    if batch_btn:
        if not batch_input.strip():
            st.warning("please enter some Arabic texts for batch analysis.")
        else:
            texts = [line.strip() for line in batch_input.split("\n") if line.strip()]

            if len(texts) > 32:
                st.warning("Batch size exceeds the limit of 32 texts. Please reduce the number of texts.")
                texts = texts[:32]
            with st.spinner(f"analyzing batch{len(texts)}texts..."):
                try:
                    responce = requests.post(
                        f"{API_url}/analyze_batch",
                        json={"texts": texts},
                        timeout=20
                    )
                    if responce.status_code ==200:
                        results=responce.json()

                        df = pd.create_dataframe(results)
                        col1,col2,col3,col4 = st.columns(4)
                        with col1:
                            st.metric("Total Texts", len(results))
                        with col2:
                            positive = sum(1 for r in results if r['sentiment'] == 'positive')
                            st.metric("Positive", positive, delta=f"{positive/len(results)*100 :.1%}")
                        with col3:
                            negative = sum(1 for r in results if r['sentiment'] == 'negative')
                            st.metric("Negative", negative, delta=f"{negative/len(results)*100 :.1%}")
                        with col4:
                            neutral = sum(1 for r in results if r['sentiment'] == 'neutral')
                            st.metric("Neutral", neutral, delta=f"{neutral/len(results)*100 :.1%}")
                        st.markdown("___")

                        for i, result in enumerate(results, 1):
                            with st.expander(f"text{i}:{result['text'][:50]}..."):
                                sentiment = result['sentiment']
                                confidence = result['confidence']
                                if sentiment == "positive":
                                    sentiment_class = "sentiment-positive"
                                    st.success(f"😊 {sentiment}")
                                elif sentiment == "negative":
                                    sentiment_class = "sentiment-negative"
                                    st.error(f"😞 {sentiment}")
                                else:
                                    sentiment_class = "sentiment-neutral"
                                    st.info(f"😐 {sentiment}")
                                st.write(f"**confidence:** {confidence:.2%}")
                                st.progress(result['confidence'])
                                st.write(f"**confidence:** {result['confidence']:.2%}")
                                st.progress(result['confidence'])
                        
                        csv =df.to_csv(index=False).encode('utf-8')
                        st.download_button(
                            label="Download CSV",
                            data=csv,
                            file_name=f"sentiment_results_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
                            mime="text/csv"
                        )

                    else:
                        st.error(f"API error: {responce.status_code}")
                except requests.exceptions.ConnectionError:
                    st.error("Failed to connect to the API. Please ensure the API is running.")
                except Exception as e:
                    st.error(f"An error occurred: {str(e)}")
with tab3:
    st.header("Model Performance")

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("accuracy metrics")

        metrics_df = pd.DataFrame({
            'Metric': ['Overall Accuracy', 'Positive Precision', 'Positive Recall', 'Negative Precision', 'Negative Recall', 'Neutral Precision', 'Neutral Recall'],
            'Score': [0.85, 0.80, 0.75, 0.90, 0.85, 0.70, 0.65]
        })
        st.dataframe(metrics_df, hide_index=True, use_container_width=True)
        st.subheader("performance")

        perf_df = pd.DataFrame({
            'metric': ['responce_time', 'Batch size', 'Model size'],
            'value': ['<100ms', 'Up to 32 texts', '500MB']
        })
        st.dataframe(perf_df, hide_index=True, use_container_width=True)

    with col2:
        st.header("model details")

        st.info("""
        **Model:** CAMeL-Lab BERT  
        **Architecture:** Transformer-based BERT  
        **parameters:** 110M
        **languages** Modern Standard Arabic (MSA)
        **Fine-tuning:** Trained on Arabic sentiment datasets  
        **Classes:** Positive, Negative, Neutral  
        **Accuracy:** ~ 87 on test set
""")

st.markdown("___")
st.markdown(
    """
    <div style="text-align:center; padding:1rem; border-radius:5px;">
            <p>Made by Saleh Ashref</p>
            <p>
            <a href='https://github.com/saleh-yasseen/Arabic_Sentiment_Analyzer'>GitHub</a> | 
            <a href='https://www.linkedin.com/in/saleh-yassien-b16256202/'>LinkedIn</a>
        </p>
    </div>
    """,
    unsafe_allow_html=True
)