from flask import Flask, render_template, request
import requests
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")
@app.route("/sentimentAnalyzer")
def sentiment_analyzer():

    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    dominant_emotion, emotions_dict, max_value = response
    output = (
       f"For the given statement, the system response is "
       f"'anger': {emotions_dict['anger']}, "
       f"'disgust': {emotions_dict['disgust']}, "
       f"'fear': {emotions_dict['fear']}, "
       f"'joy': {emotions_dict['joy']} and "
       f"'sadness': {emotions_dict['sadness']}. "
       f"The dominant emotion is {dominant_emotion}"
    )
    return output

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template('index.html')

if __name__ == "__main__":
    ''' This functions executes the flask app and deploys it on localhost:5000
    '''
    app.run(host="0.0.0.0", port=5000)
