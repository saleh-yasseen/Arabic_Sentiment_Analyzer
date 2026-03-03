from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional

from Arabic_sentiment_analyzer_App import ArabicSentimentAnalyzer

app = FastAPI()


class TextRequest(BaseModel):
    text: str


class BatchRequest(BaseModel):
    texts: List[str]


analyzer: Optional[ArabicSentimentAnalyzer] = None


@app.on_event("startup")
async def load_model():
    global analyzer
    if analyzer is None:
        analyzer = ArabicSentimentAnalyzer()


@app.get("/")
async def root():
    return {
        "message": "Arabic Sentiment Analyzer API",
        "usage": "POST /analyze {\"text\": \"...\" } or POST /analyze/batch {\"texts\": [...] }",
    }


@app.post("/analyze")
async def analyze(req: TextRequest):
    if analyzer is None:
        return {"error": "model not loaded"}
    result = analyzer.analyze(req.text)
    return result


@app.post("/analyze/batch")
async def analyze_batch(req: BatchRequest):
    if analyzer is None:
        return {"error": "model not loaded"}
    return analyzer.analyze_batch(req.texts)