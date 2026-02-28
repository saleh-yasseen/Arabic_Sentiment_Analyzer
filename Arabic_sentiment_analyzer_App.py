import transformers
from transformers import pipeline
import torch

class ArabicSentimentAnalyzer:
    def __init__(self):
        print("Loading model...")
        self.classifier = pipeline(
            "sentiment-analysis",
            model="CAMeL-Lab/bert-base-arabic-camelbert-msa-sentiment"
        )
        print("Model loaded successfully!")
    
    def analyze(self, text):
        if not text or len(text.strip())==0:
            return{"error":"no text provided for analysis"}
        result = self.classifier(text)[0]

        return{
            'text': text,
            'sentiment': result['label'],
            'confidence':round(result['score'],4),
            'confident': result['score'] > 0.8
        }
    
    def analyze_batch(self, texts):
        results = []
        for text in texts:
            results.append(self.analyze(text))
        return results
    
    def get_statistics(self, results):
        if not results:
            return {}
        
        sentiments = [r['sentiment'] for r in results if 'sentiment' in r]
        
        from collections import Counter
        counts = Counter(sentiments)
        
        return {
            "total": len(results),
            "positive": counts.get('positive', 0),
            "negative": counts.get('negative', 0),
            "neutral": counts.get('neutral', 0),
            "average_confidence": sum(r['confidence'] for r in results if 'confidence' in r) / len(results)
        }

def interactive():
    analyzer = ArabicSentimentAnalyzer()
    print("\n" + "="*60)
    print("ArabicSentimentAnalyzer interactive mode")
    print("\n" + "="*60)
    print("enter arabic text (or 'quit' to exit)")

    while True:
        user_input = input("\narabic text:")
        if user_input.strip().lower() == 'quit':
            print('goodbye!')
            break

        if not user_input.strip():
            print("enter text")
            continue

        result = analyzer.analyze(user_input)
        if isinstance(result, dict) and 'error' in result:
            print(f"error:{result['error']}")
        else:
            print(f"\n sentiment: {result['sentiment']}")
            print(f"confidence:{result['confidence']*100:.2f}%")

            if result['confident']:
                print("high confidence prediction")
            else:
                print("low confidence model is not certain")
interactive()