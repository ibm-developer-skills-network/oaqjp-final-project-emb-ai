import requests
import json

def emotion_detector(text_to_analyse):
    null_result = {
        'anger': None,
        'disgust': None,
        'fear': None,
        'joy': None,
        'sadness': None,
        'dominant_emotion': None
    }

    if not text_to_analyse:
        return result

    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = { "raw_document": { "text": text_to_analyse } }
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    
    try:
        response = requests.post(url, json = myobj, headers=header)
        formatted_response = json.loads(response.text)
        if(response.status_code == 400):
            return null_result

    
        emotion_predictions = formatted_response.get('emotionPredictions', [])
        first_prediction = emotion_predictions[0]
        emotions = first_prediction.get('emotion', {})

        # Extract individual emotion scores
        anger_score = emotions.get('anger', 0)
        disgust_score = emotions.get('disgust', 0)
        fear_score = emotions.get('fear', 0)
        joy_score = emotions.get('joy', 0)
        sadness_score = emotions.get('sadness', 0)

        dominant_emotion = max(emotions, key=emotions.get)

        result = {
            'anger': anger_score,
            'disgust': disgust_score,
            'fear': fear_score,
            'joy': joy_score,
            'sadness': sadness_score,
            'dominant_emotion': dominant_emotion
        }
        return result

    except Exception  as e:
        return null_result



# from emotion_detection import emotion_detector
# emotion_detector("I am so happy I am doing this")
