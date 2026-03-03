# Arabic Sentiment Analyzer

![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-green?logo=fastapi)
![PyTorch](https://img.shields.io/badge/PyTorch-2.0+-red?logo=pytorch)
![License](https://img.shields.io/badge/License-CC%20BY--SA%204.0-yellow)

A production-ready FastAPI application for Arabic sentiment analysis using state-of-the-art transformer models.
___

## Performance

- **Accuracy**: ~87% on test set
- **Languages**: Modern Standard Arabic (MSA)
- **Response Time**: < 100ms per request
- **Batch Size**: Up to 32 texts per request

## Features

- **Single Text Analysis**: Analyze sentiment of a single Arabic text
- **Batch Processing**: Analyze sentiment of multiple texts in one request
- **Confidence Scores**: Get sentiment confidence scores for each prediction
- **Pre-trained Model**: Uses CAMeL-Lab's BERT model trained on Arabic sentiment data

## Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Setup

1. Clone the repository:
```bash
git clone https://github.com/saleh-yasseen/Arabic_Sentiment_Analyzer
cd arabic_sentiment_analyzer
```

2. Create a virtual environment (optional but recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Running the API

Start the FastAPI server:
```bash
fastapi dev main.py
```

The API will be available at `http://localhost:8000`

### API Endpoints

#### Root Endpoint
- **GET** `/`
  - Returns API information and usage instructions

#### Analyze Single Text
- **POST** `/analyze`
  - Request body:
    ```json
    {
      "text": "نص عربي للتحليل"
    }
    ```
  - Response:
    ```json
    {
      "text": "نص عربي للتحليل",
      "sentiment": "POSITIVE",
      "confidence": 0.95,
      "confident": true
    }
    ```

#### Analyze Batch
- **POST** `/analyze/batch`
  - Request body:
    ```json
    {
      "texts": ["نص أول", "نص ثاني"]
    }
    ```
  - Response: Array of sentiment analysis results

## Model Information

- **Model**: CAMeL-Lab BERT Base Arabic (bert-base-arabic-camelbert-mix-sentiment)
- **Task**: Sentiment Classification
- **Classes**: POSITIVE, NEGATIVE, NEUTRAL
- **Auto-downloaded**: The model is automatically downloaded on first run

## Project Structure

```
arabic_sentiment_analyzer/
├── main.py                          # FastAPI application
├── Arabic_sentiment_analyzer_App.py  # Sentiment analyzer class
├── Postman_Collection.json          # Postman API collection
├── sentiment_analyzer.ipynb         # Jupyter notebook experiments
├── requirements.txt                 # Project dependencies
├── README.md                        # This file
├── .gitignore                       # Git ignore rules
└── model/                           # Model files (auto-downloaded)
    ├── config.json
    ├── tf_model.h5
    ├── tokenizer_config.json
    ├── special_tokens_map.json
    └── vocab.txt
```

## Dependencies

- **fastapi**: Modern web framework for building APIs
- **pydantic**: Data validation using Python type annotations
- **transformers**: NLP library with pre-trained models
- **torch**: Deep learning framework
- **huggingface-hub**: Download models from Hugging Face
- **uvicorn**: ASGI web server

## Testing

Use the provided Postman collection (`Postman_Collection.json`) to test the API endpoints, or use curl:

```bash
# Single text analysis
curl -X POST "http://localhost:8000/analyze" \
  -H "Content-Type: application/json" \
  -d '{"text": "هذا نص رائع جداً"}'

# Batch analysis
curl -X POST "http://localhost:8000/analyze/batch" \
  -H "Content-Type: application/json" \
  -d '{"texts": ["نص جيد", "نص سيء"]}'
```

## License

This project uses the CAMeL-Lab BERT model which is available under the CC BY-SA 4.0 license.

## Contributing

Feel free to submit issues and enhancements!
