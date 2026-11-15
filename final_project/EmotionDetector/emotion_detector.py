"""
Emotion Detector Application

This module detects emotions from the given text
using an emotion detection API.
"""

# Parsing HTTP response
import json

# Handling http request
import requests


def emotion_detector(text_to_analyse):
    """
    Analyze the text and share the emotion score
    """

    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    myobj = {"raw_document": {"text": text_to_analyse}}
    # Set the headers required for the API request
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    # Send a POST request to the API with the text and headers
    response = requests.post(url, json=myobj, headers=header, timeout=30)
    if response.status_code == 400:
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None,
        }

    formatted_response = json.loads(response.text)
    emotion_scores = {
        "anger": formatted_response["emotionPredictions"][0]["emotion"]["anger"],
        "disgust": formatted_response["emotionPredictions"][0]["emotion"]["disgust"],
        "fear": formatted_response["emotionPredictions"][0]["emotion"]["fear"],
        "joy": formatted_response["emotionPredictions"][0]["emotion"]["joy"],
        "sadness": formatted_response["emotionPredictions"][0]["emotion"]["sadness"],
    }
    emotion_scores["dominant_emotion"] = max(emotion_scores, key=emotion_scores.get)
    return emotion_scores
