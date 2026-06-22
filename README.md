# Mental Health Chatbot using Flask and spaCy

This project is a simple AI-powered Mental Health Chatbot built using Flask and spaCy. The chatbot analyzes user messages to identify basic emotional states such as sadness, happiness, and stress, and responds with supportive and encouraging messages.

## Features
* REST API built with Flask.
* Basic sentiment detection using keyword-based analysis.
* Uses spaCy for Natural Language Processing (NLP).
* Provides predefined supportive responses based on detected emotions.
* Returns responses in JSON format, making it easy to integrate with web or mobile applications.

## Supported Emotions

* Sad
* Happy
* Stressed
* Neutral (default response)

## Tech Stack

* Python
* Flask
* spaCy
* REST API

## How It Works

1. The user sends a message to the `/chat` endpoint.
2. The chatbot analyzes the message to determine the user's emotional state.
3. Based on the detected sentiment, a supportive response is selected randomly from predefined responses.
4. The response is returned as a JSON object.

This project serves as a foundation for building more advanced mental health support systems by integrating machine learning models, emotion detection, and conversational AI techniques.
