import json
import requests


def emotion_detector(text_to_analyze):
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, headers=header, json=myobj)
    if response.status_code == 400:
        return dict.fromkeys(["anger", "disgust", "fear", "joy", "sadness", "dominant_emotion"], None)
    formatted_response = json.loads(response.text)
    emotions = formatted_response["emotionPredictions"][0]["emotion"]
    dominant_emotion = max(emotions, key=emotions.get)
    return {**emotions, "dominant_emotion": dominant_emotion}
