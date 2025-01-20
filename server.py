"""
Weriya Joseph Masao
Emotion_Detection_Program
20/01/2025

"""
from flask import Flask, render_template, request
import requests
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/sentimentAnalyzer")
def sentiment_analyzer():
    ''' This code receives the text from the HTML interface and runs sentiment analysis over it '''
    text_to_analyze = request.args.get('textToAnalyze')
    if not text_to_analyze:  # Error handling for blank input
        return "Invalid text! Please try again!"
    try:
        response = emotion_detector(text_to_analyze)
        # Check if the response is valid and not empty
        if response[0] is None:
            return "Invalid text! Please try again!"
        dominant_emotion, emotions_dict = response
        output = (
            f"For the given statement, the system response is"
            f"'anger': {emotions_dict['anger']},"
            f"'disgust': {emotions_dict['disgust']},"
            f"'fear': {emotions_dict['fear']},"
            f"'joy': {emotions_dict['joy']} and"
            f"'sadness': {emotions_dict['sadness']}."
            f"The dominant emotion is {dominant_emotion}"
        )
        return output

    except requests.exceptions.RequestException:
        # Error handling if the external request fails (e.g., status_code = 400)
        emotions_dict = {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None
        }
        return (
            f"For the given statement, the system response is "
            f"'anger': {emotions_dict['anger']}, "
            f"'disgust': {emotions_dict['disgust']}, "
            f"'fear': {emotions_dict['fear']}, "
            f"'joy': {emotions_dict['joy']} and "
            f"'sadness': {emotions_dict['sadness']}. "
            f"The dominant emotion is None"
        )

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the 
    main application page over the Flask channel '''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
