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

## Docker Setup

### Prerequisites
- Docker and Docker Compose installed

### Running with Docker

1. Build and run the services:
```bash
docker-compose up --build
```

2. Access the applications:
- **Streamlit App**: http://localhost:8501
- **FastAPI API**: http://localhost:8000

The Streamlit app will automatically connect to the API running in the container.

### Stopping the Services

```bash
docker-compose down
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
├── streamlit_app.py                 # Streamlit web interface
├── Postman_Collection.json          # Postman API collection
├── sentiment_analyzer.ipynb         # Jupyter notebook experiments
├── requirements.txt                 # Project dependencies
├── Dockerfile                       # Docker container configuration
├── docker-compose.yml               # Docker Compose orchestration
├── .dockerignore                    # Docker ignore rules
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
- **streamlit**: Web app framework for data apps
- **requests**: HTTP library for API calls
- **pandas**: Data manipulation library

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


Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## Contact

**Saleh Ashref**
- GitHub: [@saleh-yasseen](https://github.com/saleh-yasseen)
- LinkedIn: [saleh-yassien](https://www.linkedin.com/in/saleh-yassien-b16256202/)
- Email: salehyassien0@gmail.com

---
