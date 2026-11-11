import json
import requests

def emotion_detector(text_to_analyze):
    if not text_to_analyze or text_to_analyze.strip() == "":
        return {
            'document': None, 'anger': None, 'disgust': None, 'fear': None,
            'joy': None, 'sadness': None, 'dominant_emotion': None, 'status_code': 400
        }

    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, json=myobj, headers=headers)
    
    formatted_response = json.loads(response.text)
    emotions = formatted_response['emotionPredictions'][0]['emotion']
    
    anger = emotions['anger']
    disgust = emotions['disgust']
    fear = emotions['fear']
    joy = emotions['joy']
    sadness = emotions['sadness']
    dominant_emotion = max(emotions, key=emotions.get)
    
    return {
        'anger': anger, 'disgust': disgust, 'fear': fear,
        'joy': joy, 'sadness': sadness, 'dominant_emotion': dominant_emotion
    }
