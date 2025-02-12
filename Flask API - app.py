from flask import Flask, request, jsonify
import spacy
import random

app = Flask(__name__)
nlp = spacy.load("en_core_web_sm")

# Predefined responses
responses = {
    "sad": ["I'm sorry you're feeling this way. Try talking to a friend or journaling your thoughts.", 
            "It's okay to feel sad sometimes. Would you like some relaxation tips?"],
    "happy": ["That's great! Keep doing what makes you feel happy!", 
              "Happiness is contagious! Spread the positivity! 😊"],
    "stressed": ["Take a deep breath. Maybe try meditation or a short walk?", 
                 "Stress is temporary. Try listening to some calming music."]
}

def analyze_sentiment(text):
    """Basic sentiment analysis"""
    doc = nlp(text.lower())
    if "sad" in text or "depressed" in text:
        return "sad"
    elif "happy" in text or "excited" in text:
        return "happy"
    elif "stressed" in text or "anxious" in text:
        return "stressed"
    else:
        return "neutral"

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message")
    sentiment = analyze_sentiment(user_input)
    response = random.choice(responses.get(sentiment, ["I'm here for you. Tell me more."]))
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
