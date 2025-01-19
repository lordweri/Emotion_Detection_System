import requests
import json
def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyse } }
    response = requests.post(url, json = myobj, headers = headers)

    formatted_response = json.loads(response.text)
    emotion_data = formatted_response['emotionPredictions'][0]['emotion']
    emotions = {
        "anger": emotion_data.get('anger', 0),
        "disgust": emotion_data.get('disgust', 0),
        "fear": emotion_data.get('fear', 0),
        "joy": emotion_data.get('joy', 0),
        "sadness": emotion_data.get('sadness', 0)
    }

    dominant_emotion = max(emotions, key=emotions.get)
    dominant_score = emotions[dominant_emotion]
    
    return dominant_emotion, dominant_score, emotions
   

 
